// ==UserScript==
// @name         MX server upload
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Adds a button to upload a map to your server.
// @author       teemann
// @match        https://tm.mania-exchange.com/tracks/*
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    var btPlay = $('.icon-play-circle.icon-large').parent();
    var lnk = btPlay.attr('href');
    var bar = btPlay.parent();
    var id = lnk.split('/');
    id = id[id.length - 1];
    bar.prepend('<a href="mxupload:' + id + '" class="btn btn-tight"><i class="icon-upload icon-large" style="position:relative;top:2px;left:3px;"></i> &nbsp;Upload to server</a>');

})();