import settings
ga_html = """
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '%s']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

<<<<<<< HEAD:analytics_middleware.py
</script></head>"""
=======
</script>"""
>>>>>>> fa5c330d807f6343e74f169a739815b9f4467c22:analytics_middleware.py

class GoogleAnalyticsMiddleware:
    def process_response(self, request, response):
        ga_id = settings.GOOGLE_ANALYTICS_ID
        if ga_id:
            current = response.content
            replacement = ga_html % ga_id
<<<<<<< HEAD:analytics_middleware.py
            response.content = current.replace("</head>", replacement)
=======
            response.content = current.replace("</body>", replacement)
>>>>>>> fa5c330d807f6343e74f169a739815b9f4467c22:analytics_middleware.py
        return response
