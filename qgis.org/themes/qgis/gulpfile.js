var gulp = require('gulp')
uglify = require('gulp-uglify'),
  concat = require('gulp-concat'),
  minifyCSS = require('gulp-minify-css');

/* Added by Tim for PureCSS - see https://purecss.io/tools/ */
grunt.loadNpmTasks('grunt-pure-grids');
grunt.initConfig({
  pure_grids: {
    dest: "assets/css/main-grid.css",
    options: {
      units: 12, // 12-column grid
      mediaQueries: {
        sm: 'screen and (min-width: 35.5em)', // 568px
        md: 'screen and (min-width: 48em)',   // 768px
        lg: 'screen and (min-width: 64em)',   // 1024px
        xl: 'screen and (min-width: 80em)',   // 1280px
        xxl: 'screen and (min-width: 120em)',  // 1920px
        xxxl: 'screen and (min-width: 160em)',  // 2560px                                    
        x4k: 'screen and (min-width: 240em)'  // 3840px                                    
      }
    }
  }
});

gulp.task('compress', function () {
  gulp.src(['assets/js/jquery.min.js', 'assets/js/jquery.prettysocial.min.js', 'assets/js/scripts.js'])
    .pipe(concat('all.min.js'))
    .pipe(uglify())
    .pipe(gulp.dest('static/js/'));
  gulp.src(['assets/css/blog.css', 'assets/css/syntax-highlighter.css', 'assets/css/custom.css'])
    .pipe(concat('all.min.css'))
    .pipe(minifyCSS())
    .pipe(gulp.dest('static/css/'));
});