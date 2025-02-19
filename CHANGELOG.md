# version 0.1.4 (2021-10-20)

- Support for custom subject in category newsletters.

# version 0.1.3 (2021-10-09)

- Development domain changed to yoogle.com
- defer js in base template

# version 0.1.2 (2021-10-05)

- Support to disable (default) the "promo code" field for new subscriptions.
- Fixes and improvements in the Article admin change form.

# version 0.1.1 (2021-10-02)

- Progressive Web Apps (PWA) support.
- "Keep reading" feature dropped.
- Many author customizations removed.
- UX improvements.
- Syntax formatting improvements and fixes on many modules and templates.
- Unneeded secure_static context processor removed.
- settings and test_settings modules improved eliminating not needed lines.
- Fixed edition PDF download view.
- Fixed Category.latest_articles method when the category has no home.
- Support for a non-subscriber version in the category newsletter preview feature.
- Support for direct path redirect in section redirect feature.
- Improvements in dashboard views.
- Support for custom templating in publications home pages.
- Support for custom headers in the to_response decorator.
- Unneeded formtools pip dependency removed.
- Support for a custom css for the print version.

# version 0.1.0 (2021-08-21)

- Django support upgraded to version 1.11 (dropped support for Django 1.5).
- Install guide upgraded, improved and tested.
- django-robots upgraded and removed from repo.
- typi submodule removed.
- Log usage and errror handling improved in send_category_nl command.
- Custom things like settings and some views were removed.
- Syntax formatting improvements and fixes on many modules.
- UX and CSS improvements in many templates.

# version 0.0.9 (2021-06-15)

- Support to exclude categories with order, from the top menu.

# version 0.0.8 (2021-06-15)

- Removed a custom attribute and method from Subscriber model.
- Renamed "costumer_id" (typo) attribute from Subscriber model to "contact_id".
- Changed urls and md5 imports to avoid deprecation warnings.
- Syntax formatting improvements on many modules.
- A deprecated-custom urls module was removed.
- Improvements on "Subscriptions" section of user profile template.
- Fixed a templatetag error when a publication does not exist.

# version 0.0.7 (2021-06-01)

- "home" app removed, categories' homes now are managed by new models in core.
- Generalizations for fields used by publications newsletters.
- Code style formatting improved on many modules.
- UX and CSS improvements in many templates.
- Generalizations for menu items for latest articles in sections, now can be defined in settings.
- Article detail view cache activated / deactivated automatically when signupwall is disabled / enabled.

# version 0.0.6 (2021-04-20)

- Unneded custom templates removed.
- Syntax improvements and de-customizations in many templates.
- More flexible subscription info in thedaily.Subscription model.
- User disabled flow changed and improved using a more friendly strategy.

# version 0.0.5 (2021-03-26)

- Dropped jquery_lazyload and using native browser load-lazy support.
- Signup support for emails upto 75 chars long (WARNING: after signup behaviour is not tested yet, may need work).
- Removed legacy customizations in ad_tag template.
- Removed share links customizations in article detail template, twitter share now uses a new Publication field.
- UX Improvements and fixes in many templates.

# version 0.0.4 (2021-03-03)

- Improvements and fixes on Category newsletters feature.
- Fixes and de-customizations for "help" and "contact" links in many templates.
- Fixes in article embed images template.

# version 0.0.3 (2021-02-17)

- tagging_autocomplete_taggit app moved to pip dependency and fixed in admin.
- Fixes to "lista de lectura" feature.
- Many improvements on article templates including also a "share" button to copy the article URL.

# version 0.0.2 (2021-01-28)

- Removed not used "inplace edit" app and related code.
- Removed not used debug app.
- Removed custom "Elegí informarte" app.
- jQuery upgraded to latest version.
- actstream, favit, ratings and updown apps moved from repo to pip dependencies.
- debug_toolbar app moved to "dev" pip dependecy.
- Removed many not used templates.
- Removed many not used tables and fields from "core" app.
- "Lista de lectura" feature. The usage of this feature is explained in https://ayuda.ladiaria.com.uy/que-es-la-lista-de-lectura/ (Spanish; la diaria's website uses utopia-cms).

# version 0.0.1 (2021-01-28)

- Initial version with the basic features.
