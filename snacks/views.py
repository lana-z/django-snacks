from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "name": "Carrots and hummus",
                "description": "Vitamin A from beta-carotene",
            }, {
                "name": "Dark chocolate",
                "description": "Iron and magnesium",
            }, {
                "name": "Almonds",
                "description": "Vitamin E",
            },
        ]
    
        return context

class AboutPageView(TemplateView):
    template_name = 'about.html'