// Custom scripts to fix theme issues
(function($) {
    // Log when script is loaded
    console.log('[MK Debug] Custom.js loaded');
    
    // Function to force image positioning
    function forceImagePositioning() {
        console.log('[MK Debug] Applying image positioning');
        
        // DIRECT APPROACH: Find the parallax background element
        // Look for a direct child with class 'bg' of the wrapper
        var $targetBg = $('#wrapper > .bg');
        console.log('[MK Debug] Found bg element:', $targetBg.length ? 'Yes' : 'No');
        
        if ($targetBg.length) {
            // Force left-aligned positioning directly on the element
            $targetBg.attr('style', $targetBg.attr('style') + '; background-position: 0% center !important; transform: none !important;');
            console.log('[MK Debug] Applied style to bg element');
        }
        
        // Handle cases where bg might be created later
        var backgroundOverrides = document.createElement('style');
        backgroundOverrides.type = 'text/css';
        backgroundOverrides.innerHTML = `
            @media screen and (max-width: 1280px) {
                #wrapper > .bg {
                    background-position: 0% center !important;
                    transform: none !important;
                }
                
                /* Target parallax elements */
                #bg {
                    background-position: 0% center !important;
                    transform: none !important;
                }
                
                /* Override any dynamic styles */
                [style*="background-position"] {
                    background-position: 0% center !important;
                }
            }
        `;
        document.head.appendChild(backgroundOverrides);
        console.log('[MK Debug] Added style overrides to head');
    }
    
    // Apply immediately on load
    $(document).ready(function() {
        console.log('[MK Debug] Document ready');
        forceImagePositioning();
        
        // Apply again after a delay to catch dynamic elements
        setTimeout(forceImagePositioning, 500);
    });
    
    // Apply again if window is resized
    $(window).on('resize', function() {
        console.log('[MK Debug] Window resized');
        forceImagePositioning();
    });
    
    // Apply on scroll to catch any lazy-loaded parallax effects
    $(window).on('scroll', function() {
        // Use throttling to avoid excessive calls
        if (!window.scrollThrottleTimeout) {
            window.scrollThrottleTimeout = setTimeout(function() {
                console.log('[MK Debug] Window scrolled');
                forceImagePositioning();
                window.scrollThrottleTimeout = null;
            }, 250);
        }
    });
    
    // Also expose the function globally for debugging
    window.forceImagePositioning = forceImagePositioning;
    
})(jQuery);