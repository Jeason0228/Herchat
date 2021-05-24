(function () {
    var noScriptMessageElement = document.getElementById('cmsg');
    var noScriptMessageText = noScriptMessageElement ? noScriptMessageElement.innerText : '';
    var getRefererQueryParamString = function () {
        try {
            var prefix = '&referer=';
            if (window.location !== window.parent.location) { // Nested Iframe
                return prefix + encodeURIComponent(window.location.href);
            }
            return prefix + encodeURIComponent(window.parent.location.href);
        } catch (e) {
            return '';
        }
    };
    var getPostCaptchaRedirectUrl = function (url) {
        if (typeof url === 'string') {
            if (url.indexOf('%3A%2F%2F' /* encoded :// */) !== -1 && dd.hsh === '1F633CDD8EF22541BD6D9B1B8EF13A') {
                return url;
            }
            return encodeURI(url);
        }
        return window.location.href;
    };

    document.write('<script>\
    if("string"==typeof navigator.userAgent&&navigator.userAgent.indexOf("Firefox")>-1)\
    {\
        var isIframeLoaded=!1,maxTimeoutMs=5e3;\
        function iframeOnload(e){\
            isIframeLoaded=!0;\
            var a=document.getElementById("noiframe");\
            a&&a.parentNode.removeChild(a)}\
            var initialTime=(new Date).getTime();\
            setTimeout(function(){\
                isIframeLoaded||(new Date).getTime()-initialTime>maxTimeoutMs&&(document.body.innerHTML=\'<div id="noiframe">' + noScriptMessageText + '</div>\'+document.body.innerHTML)},maxTimeoutMs)}else function iframeOnload(){}</script><iframe src="https://' + dd.host + '/captcha/?initialCid=' + encodeURIComponent(dd.cid) + '&hash=' + encodeURIComponent(dd.hsh) + '&cid=' + encodeURIComponent(function () { var r = new RegExp("datadome=([^;]+)"); var v = r.exec(document.cookie); if (v != null) try { return decodeURIComponent(v[1]) } catch (e) { return v[1]; } return null; }()) + '&t=' + encodeURIComponent(dd.t) + getRefererQueryParamString() + '&s=' + dd.s + '" width="100%" height="100%" style="height:100vh;" FRAMEBORDER="0" border="0" scrolling="yes" onload="iframeOnload()"></iframe>');

    if (noScriptMessageElement) {
        noScriptMessageElement.parentNode.removeChild(noScriptMessageElement);
    }
    var shouldBack = (dd.r && dd.r === 'b' && window.history && typeof window.history.back === 'function' && window.history.length > 1);
    var viewPortTag = document.createElement('meta');
    viewPortTag.name = "viewport";
    viewPortTag.content = "width=device-width, initial-scale=1.0";
    var headTags = document.getElementsByTagName('head');
    if (headTags.length > 0) {
        headTags[0].appendChild(viewPortTag);
    }
    var setupCaptchaCookieCallBack = function (event) {
        if (typeof event.data !== 'string') {
            return false;
        }
        var data = JSON.parse(event.data);
        document.cookie = data.cookie;
        var hasGoneBack = false;
        if (data.url) {
            // Reload the page
            setTimeout(function () {
                if (typeof ddReloadPageCustom === 'function') {
                    ddReloadPageCustom();
                } else if (shouldBack) {
                    history.back();
                    hasGoneBack = true;
                } else {
                    window.location.href = getPostCaptchaRedirectUrl(data.url);
                }
            }, 500);

            if (typeof ddReloadPageCustom !== 'function') {
                setTimeout(function () {
                    if (!hasGoneBack) {
                        window.location.reload();
                    }
                }, 750)
            }
        }
    };
    if (window.addEventListener) {
        window.addEventListener('message', setupCaptchaCookieCallBack, false);
    } else if (window.attachEvent) {
        window.attachEvent('onmessage', setupCaptchaCookieCallBack);
    }
})();
