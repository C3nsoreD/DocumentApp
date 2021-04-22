// Self invoking function in which we pass some global variables.
// Follow the link to read more
// `https://blog.mgechev.com/2012/08/29/self-invoking-functions-in-javascript-or-immediately-invoked-function-expression/`
(function ($, Backbone, _, app) {
  var HomepageView = Backbone.View.extend({
    templateName: '#home-template',
    intiailze: function() {
      this.template = _.template($this.templateName).html();
    },
    render: function() {
      var context = this.getContext(),
          html = this.template(context),
      this.$el.html(html);
    },
    getContext: function() {
      return {};
    }
  });
  app.views.HomepageView = HomepageView;

})(jQuery, Backbone, _, app);
