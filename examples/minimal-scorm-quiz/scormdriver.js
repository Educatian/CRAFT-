(function () {
  function findApiInParents(win) {
    var maxTries = 20;
    var current = win;
    var tries = 0;

    while (current && tries < maxTries) {
      try {
        if (current.API) {
          return current.API;
        }
        tries += 1;
        if (current.parent && current.parent !== current) {
          current = current.parent;
        } else {
          break;
        }
      } catch (error) {
        // An LMS may embed the SCO below a cross-origin frame. That frame
        // cannot be inspected; keep browser-only preview available.
        break;
      }
    }

    return null;
  }

  function findApi(win) {
    var api = findApiInParents(win);
    if (api) {
      return api;
    }
    try {
      return findApiInParents(win.opener);
    } catch (error) {
      return null;
    }
  }

  function createDriver() {
    var api = null;
    var initialized = false;

    function safeCall(fn, fallback) {
      try {
        return fn();
      } catch (error) {
        console.warn("SCORM call failed", error);
        return fallback;
      }
    }

    return {
      init: function () {
        if (initialized) {
          return true;
        }

        api = findApi(window);
        if (!api) {
          console.warn("No SCORM 1.2 API found. Running in browser-only mode.");
          return false;
        }

        initialized = safeCall(function () {
          return api.LMSInitialize("") === "true";
        }, false);
        return initialized;
      },

      finish: function () {
        if (!api || !initialized) {
          return false;
        }
        return safeCall(function () {
          return api.LMSFinish("") === "true";
        }, false);
      },

      get: function (element) {
        if (!api || !initialized) {
          return "";
        }
        return safeCall(function () {
          return api.LMSGetValue(element) || "";
        }, "");
      },

      set: function (element, value) {
        if (!api || !initialized) {
          return false;
        }
        return safeCall(function () {
          return api.LMSSetValue(element, String(value)) === "true";
        }, false);
      },

      commit: function () {
        if (!api || !initialized) {
          return false;
        }
        return safeCall(function () {
          return api.LMSCommit("") === "true";
        }, false);
      },

      setStatus: function (status) {
        return this.set("cmi.core.lesson_status", status);
      },

      setScore: function (raw, min, max) {
        this.set("cmi.core.score.raw", raw);
        this.set("cmi.core.score.min", min);
        this.set("cmi.core.score.max", max);
      },

      setLocation: function (location) {
        return this.set("cmi.core.lesson_location", location);
      },

      setSuspendData: function (value) {
        return this.set("cmi.suspend_data", value);
      },

      getSuspendData: function () {
        return this.get("cmi.suspend_data");
      },

      setExit: function (value) {
        return this.set("cmi.core.exit", value);
      }
    };
  }

  window.scorm12 = createDriver();
})();
