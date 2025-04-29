(function () {
    const CONSENT_NAME = "_ga_consent";
    const ONE_YEAR = 60 * 60 * 24 * 365;
  
    function getCookie(name) {
      return document.cookie
        .split("; ")
        .find((row) => row.startsWith(name + "="))
        ?.split("=")[1];
    }
  
    function loadGA() {
      if (window.GA_INITIALIZED) return;
      window.GA_INITIALIZED = true;
  
      const s = document.createElement("script");
      s.src = "https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX"; // Sustituye con tu ID real
      s.async = true;
      document.head.appendChild(s);
  
      window.dataLayer = window.dataLayer || [];
      function gtag() {
        dataLayer.push(arguments);
      }
      gtag("js", new Date());
      gtag("config", "G-XXXXXXX", { anonymize_ip: true });
    }
  
    document.addEventListener("DOMContentLoaded", () => {
      const consent = getCookie(CONSENT_NAME);
  
      if (consent === "true") {
        loadGA();
        return;
      }
  
      const banner = document.getElementById("cookie-banner");
      if (!banner) return;
  
      banner.style.display = "block";
  
      const btnAccept = document.getElementById("btn-accept");
      const btnReject = document.getElementById("btn-reject");
  
      if (btnAccept) {
        btnAccept.addEventListener("click", () => {
          document.cookie = `${CONSENT_NAME}=true; max-age=${ONE_YEAR}; path=/; samesite=Lax`;
          loadGA();
          banner.remove();
        });
      }
  
      if (btnReject) {
        btnReject.addEventListener("click", () => {
          document.cookie = `${CONSENT_NAME}=false; max-age=${ONE_YEAR}; path=/; samesite=Lax`;
          banner.remove();
        });
      }
    });
  })();
  