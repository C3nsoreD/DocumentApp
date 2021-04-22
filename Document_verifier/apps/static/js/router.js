(function($, backbone, _, app) {
  var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'home'
    },
    intiailze: function(options) {
      this.contentElement = "#content";   // the ID selector for underscore.js template
      this.current = null;
      Backbone.history.start();
    },
    // Home function renders the hompage view that is specified in app
    home: function() {
      var view = new app.views.HomepageView({el: this.contentElement});
      this.render(view);
    },
    // Function keeps track of which view to display
    render: function(view) {
      if (this.current) {
        this.current.$el = $();
        this.current.remove();
      }
      this.current = view;
      this.current.render();
    }
  });

  app.router = AppRouter;   // Attached router to app making it avaiable to the project

})(jQuery, backbone, _, app);
