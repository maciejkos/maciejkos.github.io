// assets/js/custom.js
console.log('[MK DEBUG] custom.js IS RUNNING - TOP LEVEL');

(function($) {
    console.log('[MK DEBUG] custom.js - IIFE RUNNING');
    $(document).ready(function() {
        console.log('[MK DEBUG] custom.js - DOCUMENT READY');
    });
})(jQuery);