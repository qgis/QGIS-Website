/**
 * Language Switcher with localStorage support
 * 
 * Features:
 * - Saves selected language to localStorage
 * - Restores language preference on next visit
 * - Updates the dropdown display to show current language
 * - Handles language redirects
 */

(function() {
  const STORAGE_KEY = 'qgis-preferred-language';
  const DEFAULT_LANG = 'en';

  /**
   * Initialize language switcher
   */
  function initLanguageSwitcher() {
    // Get the current language from the URL or default to English
    const currentLang = getCurrentLanguage();
    
    // Update the display
    updateLanguageDisplay(currentLang);
    
    // Restore saved preference if on homepage/root and no language prefix
    restoreSavedLanguage();
    
    // Add event listeners to language options
    attachLanguageSwitchListeners();
  }

  /**
   * Get current language from URL
   */
  function getCurrentLanguage() {
    const pathname = window.location.pathname;
    const parts = pathname.split('/').filter(Boolean);
    
    // Check if first part is a language code
    if (parts.length > 0) {
      const langPattern = /^[a-z]{2}(-[a-z]{2,}|_[a-z]{2})?$/i; // Matches 'en', 'pt-br', 'pt_br', 'zh-hans', etc.
      if (langPattern.test(parts[0])) {
        return parts[0];
      }
    }
    
    return DEFAULT_LANG;
  }

  /**
   * Update the dropdown display to show current language
   */
  function updateLanguageDisplay(lang) {
    const display = document.getElementById('current-lang-display');
    if (!display) return;
    
    // Find the language option that matches
    const langOption = document.querySelector(`[data-lang="${lang}"]`);
    if (langOption) {
      display.textContent = langOption.textContent;
    }
  }

  /**
   * Restore saved language preference
   * Redirects to saved language if on root path and coverage is sufficient
   */
  function restoreSavedLanguage() {
    const savedLang = localStorage.getItem(STORAGE_KEY);
    
    if (!savedLang || savedLang === DEFAULT_LANG) {
      return; // No saved preference or saved as English
    }
    
    // Check if we're on a non-prefixed URL (root or English content)
    const pathname = window.location.pathname;
    const parts = pathname.split('/').filter(Boolean);
    
    // If already on a language-prefixed URL, don't redirect
    const langPattern = /^[a-z]{2}(-[a-z]{2,}|_[a-z]{2})?$/i;
    if (parts.length > 0 && langPattern.test(parts[0])) {
      return; // Already on a language-prefixed URL
    }
    
    // Redirect to saved language if not already there
    if (savedLang !== DEFAULT_LANG) {
      const newPath = `/${savedLang}${pathname}`;
      window.location.href = newPath;
    }
  }

  /**
   * Attach click listeners to language options
   */
  function attachLanguageSwitchListeners() {
    const langOptions = document.querySelectorAll('.lang-option');
    
    langOptions.forEach(option => {
      option.addEventListener('click', function(e) {
        e.preventDefault();
        
        const lang = this.getAttribute('data-lang');
        const langName = this.textContent;
        
        // Save to localStorage
        if (lang === DEFAULT_LANG) {
          localStorage.removeItem(STORAGE_KEY);
        } else {
          localStorage.setItem(STORAGE_KEY, lang);
        }
        
        // Update display
        updateLanguageDisplay(lang);
        
        // Navigate to the language version
        navigateToLanguage(lang);
      });
    });
  }

  /**
   * Navigate to the selected language version of the page
   */
  function navigateToLanguage(lang) {
    let currentPath = window.location.pathname;
    
    // Remove language prefix if it exists
    const parts = currentPath.split('/').filter(Boolean);
    const langPattern = /^[a-z]{2}(-[a-z]{2,}|_[a-z]{2})?$/i;
    
    if (parts.length > 0 && langPattern.test(parts[0])) {
      // Remove the language prefix
      parts.shift();
      currentPath = '/' + parts.join('/');
    }
    
    // Construct new path with language prefix
    if (lang === DEFAULT_LANG) {
      // English: no language prefix
      window.location.href = currentPath || '/';
    } else {
      // Other languages: add language prefix
      window.location.href = `/${lang}${currentPath}`;
    }
  }

  /**
   * Handle dropdown click to close on item selection
   */
  function setupDropdownBehavior() {
    const langOptions = document.querySelectorAll('.lang-option');
    const dropdown = document.getElementById('language-dropdown');
    
    langOptions.forEach(option => {
      option.addEventListener('click', function() {
        // Close dropdown after selection
        if (dropdown) {
          dropdown.classList.remove('is-active');
        }
      });
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
      initLanguageSwitcher();
      setupDropdownBehavior();
    });
  } else {
    initLanguageSwitcher();
    setupDropdownBehavior();
  }
})();
