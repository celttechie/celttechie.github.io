/**
 * Interactive Deep-Linking & Auto-Tab Activation for MkDocs Material
 * Enables jumping directly to anchors located inside inactive tabs.
 */
document.addEventListener("DOMContentLoaded", function () {
  function activateAndScrollTo(hash) {
    if (!hash || hash === "#") return;

    // Remove leading #
    const elementId = hash.startsWith("#") ? hash.substring(1) : hash;
    const target = document.getElementById(elementId) || document.querySelector(hash);
    if (!target) return;

    // Check if target is inside a tabbed block
    const tabbedBlock = target.closest(".tabbed-block");
    if (tabbedBlock) {
      const tabbedSet = tabbedBlock.closest(".tabbed-set");
      if (tabbedSet) {
        // Find index of this block
        const blocks = Array.from(tabbedSet.querySelectorAll(".tabbed-block"));
        const blockIndex = blocks.indexOf(tabbedBlock);

        if (blockIndex >= 0) {
          // Switch tab via radio input
          const radioInputs = tabbedSet.querySelectorAll("input[type='radio']");
          if (radioInputs[blockIndex]) {
            radioInputs[blockIndex].checked = true;
            radioInputs[blockIndex].dispatchEvent(new Event("change", { bubbles: true }));
          }

          // Switch tab via labels if present
          const labels = tabbedSet.querySelectorAll(".tabbed-labels > *");
          if (labels[blockIndex]) {
            labels[blockIndex].click();
          }
        }
      }
    }

    // Scroll to the target element after layout updates
    setTimeout(function () {
      const parentRow = target.closest("tr") || target.closest("li") || target;
      
      // Trigger pulse animation
      parentRow.classList.remove("target-pulse-active");
      void parentRow.offsetWidth; // Trigger reflow
      parentRow.classList.add("target-pulse-active");

      // Smooth scroll into center view
      parentRow.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 60);
  }

  // Intercept all internal hash link clicks
  document.addEventListener("click", function (e) {
    const anchor = e.target.closest("a");
    if (anchor) {
      const href = anchor.getAttribute("href");
      if (href && href.startsWith("#")) {
        // Allow default hash navigation or handle explicitly
        activateAndScrollTo(href);
      }
    }
  });

  // Handle direct loads with hash in URL
  if (window.location.hash) {
    activateAndScrollTo(window.location.hash);
  }

  // Handle browser back/forward buttons
  window.addEventListener("hashchange", function () {
    if (window.location.hash) {
      activateAndScrollTo(window.location.hash);
    }
  });
});
