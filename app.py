from flask import Flask, request, jsonify
import json
from DSPrompter import DSPrompter

app = Flask(__name__)
dsp = DSPrompter()

def read_file_skip_errors(file_path, encoding='utf-8'): #encoding errors from html >:(
    try:
        with open(file_path, 'r', encoding=encoding, errors='replace') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

@app.route('/')
def test_good():
    return jsonify({"response": "good"})


@app.route('/test')
def test():
    test_instruct = {
        "htmlCode": test_file(),
        "instruction": "I want to go to my data structures and algorithms class"
    }

    json_response = dsp.get_json_response_from_dict_instruction(test_instruct)
    print("type:")
    print(type(json_response))
    print(json_response)

    return jsonify(json_response)


@app.route('/ask', methods=['POST'])
def ask():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    json_obj = request.get_json()
    json_response = dsp.get_json_response_from_dict_instruction(json_obj)
    return jsonify(json_response)

if __name__ == '__main__':
    app.run(debug=True)

def test_file():
    return \
"""
<!DOCTYPE html>
<html dir="ltr" lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#003459">
  
  <meta name="robots" content="noindex,nofollow" />
  <meta name="apple-itunes-app" content="app-id=480883488">
<link rel="manifest" href="/web-app-manifest/manifest.json">
  <meta name="sentry-trace" content="849d8e1e451d4e298ced69e044d2bf81-8b8827d1868d4fab-0"/>
  <title>Dashboard</title>

  <link rel="preload" href="https://du11hjcvx0uqb.cloudfront.net/dist/fonts/lato/extended/Lato-Regular-bd03a2cc27.woff2" as="font" type="font/woff2" crossorigin="anonymous">
  <link rel="preload" href="https://du11hjcvx0uqb.cloudfront.net/dist/fonts/lato/extended/Lato-Bold-cccb897485.woff2" as="font" type="font/woff2" crossorigin="anonymous">
  <link rel="preload" href="https://du11hjcvx0uqb.cloudfront.net/dist/fonts/lato/extended/Lato-Italic-4eb103b4d1.woff2" as="font" type="font/woff2" crossorigin="anonymous">
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/no_variables/bundles/fonts-6ee09b0b2f.css" media="screen" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/85a7aa64f74764bc6e139c616e6ff7fd/variables-7dd4b80918af0e0218ec0229e4bd5873.css" media="all" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/common-fa431f64c6.css" media="all" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/react_todo_sidebar-df089b77a5.css" media="screen" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/dashboard-a8b88f8512.css" media="screen" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/dashboard_card-c77dbc9c96.css" media="screen" />
  <link rel="stylesheet" href="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/new_user_tutorials-6b15f87caf.css" media="screen" />
  <link rel="apple-touch-icon" href="https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23355/KUlogo-mobile-icon.png" />
  <link rel="icon" type="image/x-icon" href="https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/931/Screen%20Shot%202020-11-12%20at%2010.49.48%20AM.png" />
  <link rel="alternate" type="application/atom+xml" title="User Atom Feed (All Courses)" href="/feeds/users/user_8npP3SLRsDORgQRGmittDSoikDIxsm5RAbBYOJOz.atom" />
  <link rel="stylesheet" href="https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/9314867/UniversityofKansasCanvasCustomCSSProductionFeb92024.css" media="all" />
  
  <script>if (navigator.userAgent.match(/(MSIE|Trident\/)/)) location.replace('/ie-is-not-supported.html')</script>
  <script>
    INST = {"environment":"production","logPageViews":true,"editorButtons":[]};
    ENV = {"ASSET_HOST":"https://du11hjcvx0uqb.cloudfront.net","active_brand_config_json_url":"https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/85a7aa64f74764bc6e139c616e6ff7fd/variables-7dd4b80918af0e0218ec0229e4bd5873.json","active_brand_config":{"md5":"85a7aa64f74764bc6e139c616e6ff7fd","variables":{"ic-brand-primary":"#0051ba","ic-brand-font-color-dark":"#333333","ic-link-color":"#0051ba","ic-brand-button--secondary-bgd":"#5c5c5c","ic-brand-global-nav-bgd":"#003459","ic-brand-global-nav-logo-bgd":"#003459","ic-brand-header-image":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23353/KUlogo-nav.png","ic-brand-mobile-global-nav-logo":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23354/KU-Favicon.png","ic-brand-watermark":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23360/Artboard-2.png","ic-brand-watermark-opacity":"0.8","ic-brand-favicon":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/931/Screen%20Shot%202020-11-12%20at%2010.49.48%20AM.png","ic-brand-apple-touch-icon":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23355/KUlogo-mobile-icon.png","ic-brand-msapplication-tile-color":"#003459","ic-brand-msapplication-tile-square":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23357/KUlogo-windows-tile.png","ic-brand-msapplication-tile-wide":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/23358/KUlogoWindows-Tile-Wide.png","ic-brand-Login-body-bgd-color":"#f2f2f2","ic-brand-Login-body-bgd-image":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/182982/canvas-login-background.jpg","ic-brand-Login-body-bgd-shadow-color":"#2d3b45","ic-brand-Login-logo":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/182983/non-ku-user-button-pick.jpg","ic-brand-Login-Content-bgd-color":"#ffffff","ic-brand-Login-Content-border-color":"#003459","ic-brand-Login-Content-label-text-color":"#0051ba","ic-brand-Login-Content-password-text-color":"#0051ba","ic-brand-Login-footer-link-color":"#0051ba"},"share":false,"name":null,"created_at":"2025-02-07T18:33:22-06:00","js_overrides":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/13062279/UniversityofKansasCanvasCustomJSProductionFeb072025.js","css_overrides":"https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/9314867/UniversityofKansasCanvasCustomCSSProductionFeb92024.css","mobile_js_overrides":"","mobile_css_overrides":"","parent_md5":null},"confetti_branding_enabled":false,"url_to_what_gets_loaded_inside_the_tinymce_editor_css":["https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/85a7aa64f74764bc6e139c616e6ff7fd/variables-7dd4b80918af0e0218ec0229e4bd5873.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_normal_contrast/bundles/what_gets_loaded_inside_the_tinymce_editor-90e5ad1077.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/no_variables/bundles/fonts-6ee09b0b2f.css"],"url_for_high_contrast_tinymce_editor_css":["https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/default/variables-high_contrast-7dd4b80918af0e0218ec0229e4bd5873.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/new_styles_high_contrast/bundles/what_gets_loaded_inside_the_tinymce_editor-795277483f.css","https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/no_variables/bundles/fonts-6ee09b0b2f.css"],"current_user_id":"90334","current_user_global_id":"191320000000090334","current_user_usage_metrics_id":"1b915cd994fe6ca4afb3c82a18d8e5c2a1f1fde08e20d55919833ef77158e506","current_user_roles":["user","student"],"current_user_is_student":false,"current_user_types":[],"current_user_disabled_inbox":false,"current_user_visited_tabs":null,"discussions_reporting":true,"files_domain":"cluster314.canvas-user-content.com","group_information":null,"DOMAIN_ROOT_ACCOUNT_ID":"191320000000000001","DOMAIN_ROOT_ACCOUNT_UUID":"vvhwb2PxzWbGfzlaTvgMnqWa1QZGm9MN43A3k1EW","k12":false,"help_link_name":"Help","help_link_icon":"help","use_high_contrast":false,"auto_show_cc":false,"disable_celebrations":false,"disable_keyboard_shortcuts":false,"LTI_LAUNCH_FRAME_ALLOWANCES":["geolocation *","microphone *","camera *","midi *","encrypted-media *","autoplay *","clipboard-write *","display-capture *"],"DEEP_LINKING_POST_MESSAGE_ORIGIN":"https://canvas.ku.edu","comment_library_suggestions_enabled":false,"SETTINGS":{"open_registration":false,"collapse_global_nav":false,"release_notes_badge_disabled":false,"can_add_pronouns":true,"show_sections_in_course_tray":true},"RAILS_ENVIRONMENT":"Production","SENTRY_FRONTEND":{"dsn":"https://355a1d96717e4038ac25aa852fa79a8f@relay-iad.sentry.insops.net/388","org_slug":"instructure","base_url":"https://sentry.insops.net","normalized_route":"/","errors_sample_rate":"0.005","traces_sample_rate":"0.005","url_deny_pattern":"instructure-uploads.*amazonaws.com","revision":"canvas-lms@20250326.308"},"DATA_COLLECTION_ENDPOINT":"https://canvas-frontend-data-iad-prod.inscloudgate.net/submit","DOMAIN_ROOT_ACCOUNT_SFID":"001A000000YwvLYIAZ","DIRECT_SHARE_ENABLED":false,"CAN_VIEW_CONTENT_SHARES":false,"FEATURES":{"account_level_blackout_dates":false,"render_both_to_do_lists":false,"commons_new_quizzes":true,"consolidated_media_player":false,"course_paces_redesign":true,"course_paces_for_students":true,"explicit_latex_typesetting":false,"media_links_use_attachment_id":true,"permanent_page_links":true,"enhanced_course_creation_account_fetching":false,"instui_for_import_page":true,"multiselect_gradebook_filters":true,"assignment_edit_placement_not_on_announcements":false,"instui_header":false,"rce_find_replace":true,"courses_popout_sisid":true,"dashboard_graphql_integration":false,"discussion_checkpoints":false,"discussion_default_sort":true,"discussion_default_expand":true,"discussion_permalink":false,"speedgrader_studio_media_capture":true,"disallow_threaded_replies_fix_alert":true,"horizon_course_setting":false,"new_quizzes_media_type":true,"differentiation_tags":false,"validate_call_to_action":false,"product_tours":true,"create_course_subaccount_picker":true,"file_verifiers_for_quiz_links":true,"lti_deep_linking_module_index_menu_modal":true,"lti_registrations_next":false,"lti_registrations_page":false,"lti_registrations_usage_data":false,"lti_asset_processor":false,"buttons_and_icons_root_account":true,"extended_submission_state":false,"scheduled_page_publication":true,"send_usage_metrics":true,"rce_transform_loaded_content":false,"mobile_offline_mode":false,"react_discussions_post":true,"instui_nav":false,"lti_registrations_discover_page":false,"account_level_mastery_scales":false,"non_scoring_rubrics":true,"top_navigation_placement":false,"rubric_criterion_range":true,"rce_lite_enabled_speedgrader_comments":true,"lti_toggle_placements":true,"login_registration_ui_identity":false,"lti_apps_page_instructors":false,"course_paces_skip_selected_days":false,"course_pace_download_document":false,"course_pace_draft_state":false,"course_pace_time_selection":false,"course_pace_pacing_status_labels":false,"course_pace_pacing_with_mastery_paths":false,"course_pace_weighted_assignments":false,"modules_requirements_allow_percentage":false,"course_pace_allow_bulk_pace_assign":false,"account_survey_notifications":false,"embedded_release_notes":false,"discussions_speedgrader_revisit":true,"canvas_k6_theme":null,"new_math_equation_handling":true},"current_user":{"id":"90334","anonymous_id":"1xpa","display_name":"Cooper S Wright","avatar_image_url":"https://canvas.ku.edu/images/thumbnails/7557473/NyPaMrDPnI09KQGmt5xwJaHF8vCa8pZ8E6ZZ91eL","html_url":"https://canvas.ku.edu/about/90334","pronouns":"He/Him","avatar_is_fallback":false,"email":"c086w012@ku.edu"},"page_view_update_url":"/page_views/a20b208a-ef80-4581-a79d-9a34c418be75?page_view_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpIjoiYTIwYjIwOGEtZWY4MC00NTgxLWE3OWQtOWEzNGM0MThiZTc1IiwidSI6MTkxMzIwMDAwMDAwMDkwMzM0LCJjIjoiMjAyNS0wNC0wNVQyMjozMDoyNi4zOVoifQ.MX6tQWadZD4p90Cy6VZnmUO1F2u9SuYVRB1Nki0-18U","context_asset_string":null,"TIMEZONE":"America/Chicago","CONTEXT_TIMEZONE":null,"LOCALES":["en"],"BIGEASY_LOCALE":"en_US","FULLCALENDAR_LOCALE":"en","MOMENT_LOCALE":"en","rce_auto_save_max_age_ms":86400000,"K5_USER":false,"USE_CLASSIC_FONT":false,"K5_HOMEROOM_COURSE":false,"K5_SUBJECT_COURSE":false,"LOCALE_TRANSLATION_FILE":"/dist/javascripts/translations/en-d4dfe69052.json","ACCOUNT_ID":"1","user_cache_key":"OG5wUDNTTFJzRE9SZ1FSR21pdHREU29pa0RJeHNtNVJBYkJZT0pPenZ5Zlc9\nO1twLTA/OntQXz1IVXBncmFxZTtuamFsa2hwdm9pdWxraW1tYXFld2c=\n","horizon_course":false,"INCOMPLETE_REGISTRATION":null,"USER_EMAIL":"c086w012@ku.edu","PREFERENCES":{"dashboard_view":"cards","hide_dashcard_color_overlays":false,"custom_colors":{"course_86717":"#177B63","course_102833":"#E71F63","course_86718":"#177B63","course_103208":"#4D3D4D","course_94472":"#009688","course_102395":"#F06291","user_90334":"#4a76b2","course_104754":"#91349B","course_106163":"#D41E00","course_101051":"#008400","course_115889":"#8f3e97","course_117346":"#009688","course_120310":"#4554a4","course_117589":"#0b9be3","course_119347":"#f06291","course_109570":"#4554a4","course_115790":"#177B63","course_115921":"#65499D","course_120552":"#324A4D","group_57104":"#ac6211","course_122430":"#324A4D","course_122958":"#D41E00","course_130208":"#65499D","course_134429":"#BD3C14","course_137864":"#06A3B7","course_128565":"#E71F63","course_139498":"#2d3e3f","course_132291":"#009606","course_146276":"#9e58bd","course_143208":"#2573df","course_152515":"#048660","course_152583":"#bf5811"}},"STUDENT_PLANNER_ENABLED":true,"STUDENT_PLANNER_COURSES":[{"longName":"F24UC Sexual Assault Prevention for Undergraduates - F24UC Sexual Assault Prevention for Undergraduate","shortName":"F24UC Sexual Assault Prevention for Undergraduates","originalName":"F24UC Sexual Assault Prevention for Undergraduates","courseCode":"F24UC Sexual Assault Prevention for Undergraduate","assetString":"course_139498","href":"/courses/139498","term":"Fall 2024","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"139498","isFavorited":false,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":null,"color":null,"position":4,"published":true,"canChangeCoursePublishState":false,"defaultView":"wiki","pagesUrl":"https://canvas.ku.edu/courses/139498/pages","frontPageTitle":"Home Page"},{"longName":"Discover KU | Fall 2023 - Discover KU","shortName":"Discover KU | Fall 2023","originalName":"Discover KU | Fall 2023","courseCode":"Discover KU","assetString":"course_86718","href":"/courses/86718","term":null,"subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"86718","isFavorited":false,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":"https://inst-fs-iad-prod.inscloudgate.net/files/7d0cadcd-7467-424f-a66a-97a45bcc69b5/KU%20Orientation.png?download=1\u0026token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NDM4MTA0NzIsInVzZXJfaWQiOm51bGwsInJlc291cmNlIjoiL2ZpbGVzLzdkMGNhZGNkLTc0NjctNDI0Zi1hNjZhLTk3YTQ1YmNjNjliNS9LVSUyME9yaWVudGF0aW9uLnBuZyIsImp0aSI6IjZiZGM0ODBmLTg3MGEtNGM2OC04MDUxLTkxY2I1YWQzMmI3YSIsImhvc3QiOm51bGwsImV4cCI6MTc0NDQxNTI3Mn0.OPDey53_jHMkw5poDN7xBCwWbYXKX6amYE6uNech6pAtv__zGfMycoGBq0tkaer1iWYtBfW8qtkgdKEuPzrg7g","color":null,"position":7,"published":true,"canChangeCoursePublishState":false,"defaultView":"wiki","pagesUrl":"https://canvas.ku.edu/courses/86718/pages","frontPageTitle":"Welcome to Discover KU"},{"longName":"Pre-Orientation | Fall 2023 - Pre-Orientation Course","shortName":"Pre-Orientation | Fall 2023","originalName":"Pre-Orientation | Fall 2023","courseCode":"Pre-Orientation Course","assetString":"course_86717","href":"/courses/86717","term":null,"subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"86717","isFavorited":false,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":"https://inst-fs-iad-prod.inscloudgate.net/files/711a4254-f860-46a8-aa10-aa82e10c4599/KU%20Orientation%20header.png?download=1\u0026token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NDM3NDUwMzMsInVzZXJfaWQiOm51bGwsInJlc291cmNlIjoiL2ZpbGVzLzcxMWE0MjU0LWY4NjAtNDZhOC1hYTEwLWFhODJlMTBjNDU5OS9LVSUyME9yaWVudGF0aW9uJTIwaGVhZGVyLnBuZyIsImp0aSI6ImY4MDVhNDc0LWVkNTAtNDM0YS1iNzY5LWNmYjA0NjIxZjM2YiIsImhvc3QiOm51bGwsImV4cCI6MTc0NDM0OTgzM30.1TQlfQs6cTJzWG1u_C06lML8pvABxjGMn6yysonHNj4Q0uymglxie9eWOfAfYEW2xyCZNRiJ0NDjFqPHyVgl9A","color":null,"position":8,"published":true,"canChangeCoursePublishState":false,"defaultView":"wiki","pagesUrl":"https://canvas.ku.edu/courses/86717/pages","frontPageTitle":"Introduction to Orientation"},{"longName":"4246-74487:HA 166 The Visual Arts of East Asia LEC - HA 166: The Visual Arts of East Asia LEC","shortName":"4246-74487:HA 166 The Visual Arts of East Asia LEC","originalName":"4246-74487:HA 166 The Visual Arts of East Asia LEC","courseCode":"HA 166: The Visual Arts of East Asia LEC","assetString":"course_122430","href":"/courses/122430","term":"Summer 2024","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"122430","isFavorited":false,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":"https://inst-fs-iad-prod.inscloudgate.net/files/c3d76059-3e90-417c-8f42-4cadef52f552/F20931A7-7F08-459E-AC49-F351E7F74DA5.jpeg?download=1\u0026token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NDM4ODQxMDksInVzZXJfaWQiOm51bGwsInJlc291cmNlIjoiL2ZpbGVzL2MzZDc2MDU5LTNlOTAtNDE3Yy04ZjQyLTRjYWRlZjUyZjU1Mi9GMjA5MzFBNy03RjA4LTQ1OUUtQUM0OS1GMzUxRTdGNzREQTUuanBlZyIsImp0aSI6ImM5MGFjYTFjLWIwMDUtNDg4ZS05NmU3LTA4ZTMzNmZjZDNlOCIsImhvc3QiOm51bGwsImV4cCI6MTc0NDQ4ODkwOX0.X9-iz1rJbm965Y-UMh5ppId-Virb9YCd7HalZdcps-WXe6rBoHfadBD1bndM49ukPY2MU1b2-bT-Rl7l3gwSZA","color":null,"position":null,"published":true,"canChangeCoursePublishState":false,"defaultView":"wiki","pagesUrl":"https://canvas.ku.edu/courses/122430/pages","frontPageTitle":"Home Page"},{"longName":"4252-40619:EECS 388 Embedded Systems LEC - EECS 388: Embedded Systems LEC","shortName":"4252-40619:EECS 388 Embedded Systems LEC","originalName":"4252-40619:EECS 388 Embedded Systems LEC","courseCode":"EECS 388: Embedded Systems LEC","assetString":"course_143208","href":"/courses/143208","term":"Spring 2025","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"143208","isFavorited":true,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":null,"color":null,"position":null,"published":true,"canChangeCoursePublishState":false,"defaultView":"wiki","pagesUrl":"https://canvas.ku.edu/courses/143208/pages","frontPageTitle":"Home Page"},{"longName":"4252-48244:JPN 208 Intermediate Japanese II LEC - JPN 208: Intermediate Japanese II LEC","shortName":"4252-48244:JPN 208 Intermediate Japanese II LEC","originalName":"4252-48244:JPN 208 Intermediate Japanese II LEC","courseCode":"JPN 208: Intermediate Japanese II LEC","assetString":"course_146276","href":"/courses/146276","term":"Spring 2025","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"146276","isFavorited":true,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":"https://inst-fs-iad-prod.inscloudgate.net/files/d50d343c-9bd9-42e2-9459-ff1e9070dd55/Screenshot%20%28267%29.png?download=1\u0026token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3NDM4MTk3NDgsInVzZXJfaWQiOm51bGwsInJlc291cmNlIjoiL2ZpbGVzL2Q1MGQzNDNjLTliZDktNDJlMi05NDU5LWZmMWU5MDcwZGQ1NS9TY3JlZW5zaG90JTIwJTI4MjY3JTI5LnBuZyIsImp0aSI6ImJmYjgxMGRmLTQ4ZjgtNDE0Mi1iYTM3LTIwNzBlODI3MDkwZiIsImhvc3QiOm51bGwsImV4cCI6MTc0NDQyNDU0OH0.eq1El6mmQ4xpo5rMeM2ozYazXf1RT4bIs6zoBx5T7iJ7KQzjLF3_NJVHMscqZXTmVUg3gdl6nVuxwP00Zv-PNw","color":null,"position":null,"published":true,"canChangeCoursePublishState":false,"defaultView":"modules","pagesUrl":"https://canvas.ku.edu/courses/146276/pages","frontPageTitle":null},{"longName":"4252-54578:EECS 330 Data Structures and Algorithms LEC - EECS 330: Data Structures and Algorithms LEC","shortName":"4252-54578:EECS 330 Data Structures and Algorithms LEC","originalName":"4252-54578:EECS 330 Data Structures and Algorithms LEC","courseCode":"EECS 330: Data Structures and Algorithms LEC","assetString":"course_152515","href":"/courses/152515","term":"Spring 2025","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"152515","isFavorited":true,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":null,"color":null,"position":null,"published":true,"canChangeCoursePublishState":false,"defaultView":"modules","pagesUrl":"https://canvas.ku.edu/courses/152515/pages","frontPageTitle":null},{"longName":"EECS 461 Probability and Statistics Spring 2025 - EECS 461 Probability and Statistics Spring 2025","shortName":"EECS 461 Probability and Statistics Spring 2025","originalName":"EECS 461 Probability and Statistics Spring 2025","courseCode":"EECS 461 Probability and Statistics Spring 2025","assetString":"course_152583","href":"/courses/152583","term":"Spring 2025","subtitle":"enrolled as: Student","enrollmentState":"active","enrollmentType":"StudentEnrollment","observee":null,"id":"152583","isFavorited":true,"isK5Subject":false,"isHomeroom":false,"useClassicFont":false,"canManage":false,"canReadAnnouncements":true,"image":null,"color":null,"position":null,"published":true,"canChangeCoursePublishState":false,"defaultView":"modules","pagesUrl":"https://canvas.ku.edu/courses/152583/pages","frontPageTitle":null}],"STUDENT_PLANNER_GROUPS":[{"id":"51831","assetString":"group_51831","name":"Final Project Group 5","url":"/groups/51831"},{"id":"57104","assetString":"group_57104","name":"Seat J-12","url":"/groups/57104"},{"id":"63196","assetString":"group_63196","name":"Mon 11a","url":"/groups/63196"},{"id":"63856","assetString":"group_63856","name":"Everyone","url":"/groups/63856"},{"id":"64843","assetString":"group_64843","name":"19","url":"/groups/64843"}],"ALLOW_ELEMENTARY_DASHBOARD":false,"CREATE_COURSES_PERMISSIONS":{"PERMISSION":null,"RESTRICT_TO_MCC_ACCOUNT":false},"OBSERVED_USERS_LIST":[{"id":"90334","name":"Cooper Wright","created_at":"2022-11-28T20:50:37-06:00","sortable_name":"Wright, Cooper S","short_name":"Cooper S Wright","pronouns":"He/Him","avatar_url":"https://canvas.ku.edu/images/thumbnails/7557473/NyPaMrDPnI09KQGmt5xwJaHF8vCa8pZ8E6ZZ91eL"}],"CAN_ADD_OBSERVEE":false,"notices":[],"active_context_tab":null};
    BRANDABLE_CSS_HANDLEBARS_INDEX = [["new_styles_normal_contrast","new_styles_high_contrast","new_styles_normal_contrast_rtl","new_styles_high_contrast_rtl"],{"10":["908ffbc673",0,"d5c9044c6e",2],"15":["c8540c43a4",0,"0a2196be1d",2],"19":["df5777ed9c"],"61":["b8f6d0d1fa","c3396c44a9","cfc0690334","1c0f3762fa"],"67":["700335fb7b",0,"1cc2485e2c",2],"71":["8ac0336ef0","bf3093677a","a8146a011b","449171073f"],"06":["ba28819778",0,"96b99aafe5",2],"f0":["b349f31f5e",0,0,0],"c8":["718c8509f5","33cd4c40e3","03d0fbcbe8","ec23096f0d"],"1e":["6eb4ecac8e","4100cb65ce","0faf4716c8","bed54fd75e"],"b3":["e5da23fb43","0911fc8ed3","05b2bb5a6f","ba2585de5c"],"0c":["4dae5befd2",0,"c18876be89",2],"da":["b5a7f9cd8f","a4e5066985","773390ae11","8e9071910c"],"1d":["2128789890",0,"e568085637",2],"08":["64bff5a97d"],"e2":["79d37f210d"],"9f":["d39b291ba6",0,0,0],"2b":["c491abf31e","b11dc54da6","b58622671f","6bb4a7ae9e"],"2c":["8a926fc28b",0,0,0],"c2":["6f2721ae01"],"9c":["c31821c764",0,"1693aba1da",2],"c5":["44c6024769","31150a4a27","53dd277fa9","5fe61c91c2"],"f2":["51574f9b13"]}]
      REMOTES = {};
  </script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/brandable_css/85a7aa64f74764bc6e139c616e6ff7fd/variables-7dd4b80918af0e0218ec0229e4bd5873.js" defer="defer"></script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/timezone/America/Chicago-d9fecf4265.js" defer="defer"></script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/timezone/en_US-80a0ce259b.js" defer="defer"></script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/react-entry-d296c7f9fc2ea0eb.js" crossorigin="anonymous" defer="defer"></script>
  <script src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/main-entry-ba2289f9369334d8.js" crossorigin="anonymous" defer="defer"></script>
<script>
//<![CDATA[
(window.bundles || (window.bundles = [])).push('dashboard');
(window.bundles || (window.bundles = [])).push('past_global_alert');
(window.bundles || (window.bundles = [])).push('navigation_header');
//]]>
</script>
  
  <script type="text/javascript">
  (function loadPendo(apiKey) {
    // Inject the Pendo agent script
    (function loadPendoAgent(global, document, tagName, namespace) {
      const pendo = global[namespace] = global[namespace] || {};
      pendo._q = pendo._q || [];

      const methods = ['initialize', 'identify', 'updateOptions', 'pageLoad', 'track'];
      methods.forEach(method => {
        pendo[method] = pendo[method] || function(...args) {
          const action = method === 'initialize' ? 'unshift' : 'push';
          pendo._q[action]([method, ...args]);
        };
      });

      const scriptElement = document.createElement(tagName);
      scriptElement.async = true;
      scriptElement.src = `https://cdn.pendo.io/agent/static/${apiKey}/pendo.js`;
      const firstScript = document.getElementsByTagName(tagName)[0];
      firstScript.parentNode.insertBefore(scriptElement, firstScript);
    })(window, document, 'script', 'pendo');

    // Delay initialization to allow the Pendo agent script to load
    setTimeout(() => {
      pendo.initialize({
        visitor: {
          id: ENV.current_user_usage_metrics_id,
          canvasRoles: ENV.current_user_roles,
          locale: ENV.LOCALE || 'en',
        },
        account: {
          id: ENV.DOMAIN_ROOT_ACCOUNT_UUID,
          surveyOptOut: ENV.FEATURES['account_survey_notifications'],
        },
      });
    }, 1000);
  })('e98d0492-f0d1-4890-79ff-5732d6f1c427');
</script>
</head>

<body class="with-right-side  primary-nav-expanded full-width context-user_90334 responsive_student_grades_page">

<noscript>
  <div role="alert" class="ic-flash-static ic-flash-error">
    <div class="ic-flash__icon" aria-hidden="true">
      <i class="icon-warning"></i>
    </div>
    <h1>You need to have JavaScript enabled in order to access this site.</h1>
  </div>
</noscript>




<div id="flash_message_holder"></div>
<div id="flash_screenreader_holder"></div>

<div id="application" class="ic-app">
  




<header id="mobile-header" class="no-print">
  <button type="button" class="Button Button--icon-action-rev Button--large mobile-header-hamburger">
    <i class="icon-solid icon-hamburger"></i>
    <span id="mobileHeaderInboxUnreadBadge" class="menu-item__badge" style="min-width: 0; top: 12px; height: 12px; right: 6px; display:none;"></span>
    <span class="screenreader-only">Dashboard</span>
  </button>
  <div class="mobile-header-space"></div>
    <span class="mobile-header-title">Dashboard</span>
    <div class="mobile-header-space"></div>
    <div class="mobile-header-space"></div>
</header>
<nav id="mobileContextNavContainer"></nav>

<header id="header" class="ic-app-header no-print " aria-label="Global Header">
  <a href="#content" id="skip_navigation_link">Skip To Content</a>
  <div role="region" class="ic-app-header__main-navigation" aria-label="Global Navigation">
      <div class="ic-app-header__logomark-container">
        <a href="https://canvas.ku.edu/" class="ic-app-header__logomark">
          <span class="screenreader-only">Dashboard</span>
        </a>
      </div>
    <ul id="menu" class="ic-app-header__menu-list">
        <li class="menu-item ic-app-header__menu-list-item ">
          <a id="global_nav_profile_link" role="button" href="/profile/settings" class="ic-app-header__menu-list-link">
            <div class="menu-item-icon-container">
              <div aria-hidden="true" class="fs-exclude ic-avatar ">
                <img src="https://canvas.ku.edu/images/thumbnails/7557473/NyPaMrDPnI09KQGmt5xwJaHF8vCa8pZ8E6ZZ91eL" alt="Cooper S Wright" />
              </div>
              <span class="menu-item__badge"></span>
            </div>
            <div class="menu-item__text">
              Account
            </div>
          </a>
        </li>
      <li class="ic-app-header__menu-list-item  ic-app-header__menu-list-item--active">
        <a id="global_nav_dashboard_link" href="https://canvas.ku.edu/" class="ic-app-header__menu-list-link">
          <div class="menu-item-icon-container" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--dashboard" version="1.1" x="0" y="0" viewBox="0 0 280 200" enable-background="new 0 0 280 200" xml:space="preserve"><path d="M273.09,180.75H197.47V164.47h62.62A122.16,122.16,0,1,0,17.85,142a124,124,0,0,0,2,22.51H90.18v16.29H6.89l-1.5-6.22A138.51,138.51,0,0,1,1.57,142C1.57,65.64,63.67,3.53,140,3.53S278.43,65.64,278.43,142a137.67,137.67,0,0,1-3.84,32.57ZM66.49,87.63,50.24,71.38,61.75,59.86,78,76.12Zm147,0L202,76.12l16.25-16.25,11.51,11.51ZM131.85,53.82v-23h16.29v23Zm15.63,142.3a31.71,31.71,0,0,1-28-16.81c-6.4-12.08-15.73-72.29-17.54-84.25a8.15,8.15,0,0,1,13.58-7.2c8.88,8.21,53.48,49.72,59.88,61.81a31.61,31.61,0,0,1-27.9,46.45ZM121.81,116.2c4.17,24.56,9.23,50.21,12,55.49A15.35,15.35,0,1,0,161,157.3C158.18,152,139.79,133.44,121.81,116.2Z" /></svg>

          </div>
          <div class="menu-item__text">
            Dashboard
          </div>
        </a>
      </li>
        <li class="menu-item ic-app-header__menu-list-item ">
          <a id="global_nav_courses_link" role="button" href="/courses" class="ic-app-header__menu-list-link">
            <div class="menu-item-icon-container" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--courses" version="1.1" x="0" y="0" viewBox="0 0 280 259" enable-background="new 0 0 280 259" xml:space="preserve"><path d="M73.31,198c-11.93,0-22.22,8-24,18.73a26.67,26.67,0,0,0-.3,3.63v.3a22,22,0,0,0,5.44,14.65,22.47,22.47,0,0,0,17.22,8H200V228.19h-134V213.08H200V198Zm21-105.74h90.64V62H94.3ZM79.19,107.34V46.92H200v60.42Zm7.55,30.21V122.45H192.49v15.11ZM71.65,16.71A22.72,22.72,0,0,0,49,39.36V190.88a41.12,41.12,0,0,1,24.32-8h157V16.71ZM33.88,39.36A37.78,37.78,0,0,1,71.65,1.6H245.36V198H215.15v45.32h22.66V258.4H71.65a37.85,37.85,0,0,1-37.76-37.76Z"/></svg>

            </div>
            <div class="menu-item__text">
              Courses
            </div>
          </a>
        </li>
        <li class="menu-item ic-app-header__menu-list-item ">
          <a id="global_nav_groups_link" role="button" href="/groups" class="ic-app-header__menu-list-link">
            <div class="menu-item-icon-container" aria-hidden="true">
              <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--groups" viewBox="0 0 200 135"><path d="M134.5 129.4c0-1.1 0-19.8-6.2-31.1-4.5-8.5-16.4-12.4-35-19.2-1.7-.6-3.4-1.1-5.1-1.7v-8.5c5.6-5.1 8.5-12.4 8.5-20.3V29.4C96.6 13 83.6 0 67.2 0S37.9 13 37.9 29.4v19.2c0 7.3 3.4 14.7 8.5 20.3v8.5c-1.7.6-3.4 1.1-5.1 1.7-18.6 6.2-30.5 10.7-35 19.2C0 109.6 0 128.8 0 129.4c0 3.4 2.3 5.6 5.6 5.6h123.7c3.5 0 5.7-2.3 5.2-5.6zm-123.2-5.7c.6-5.6 1.7-14.7 3.4-19.8C17 98.8 30 94.3 43.5 89.8c2.8-1.1 5.6-2.3 9-3.4 2.3-.6 4-2.8 4-5.1V66.7c0-1.7-.6-3.4-1.7-4.5-4-3.4-6.2-8.5-6.2-13.6V29.4c0-10.2 7.9-18.1 18.1-18.1s18.1 7.9 18.1 18.1v19.2c0 5.1-2.3 10.2-6.2 13.6-1.1 1.1-1.7 2.8-1.7 4.5v14.7c0 2.3 1.7 4.5 4 5.1 2.8 1.1 6.2 2.3 9 3.4 13.6 5.1 26.6 9.6 28.8 14.1 2.8 5.1 4 13.6 4.5 19.8H11.3zM196 79.1c-2.8-6.2-11.3-9.6-22.6-13.6l-1.7-.6v-3.4c4.5-4 6.8-9.6 6.8-15.8V35c0-12.4-9.6-22-22-22s-22 10.2-22 22v10.7c0 6.2 2.3 11.9 6.8 15.8V65l-1.7.6c-7.3 2.8-13 4.5-16.9 7.3-1.7 1.1-2.3 2.8-2.3 5.1.6 1.7 1.7 3.4 3.4 4.5 7.9 4 12.4 7.3 14.1 10.7 2.3 4.5 4 10.2 5.1 18.1.6 2.3 2.8 4.5 5.6 4.5h45.8c3.4 0 5.6-2.8 5.6-5.1 0-3.9 0-24.3-4-31.6zm-42.9 25.4c-1.1-6.8-2.8-12.4-5.1-16.9-1.7-4-5.1-6.8-9.6-10.2 1.7-1.1 3.4-1.7 5.1-2.3l5.6-2.3c1.7-.6 3.4-2.8 3.4-5.1v-9.6c0-1.7-.6-3.4-2.3-4.5-2.8-1.7-4.5-5.1-4.5-8.5V34.5c0-6.2 4.5-10.7 10.7-10.7s10.7 5.1 10.7 10.7v10.7c0 3.4-1.7 6.2-4.5 8.5-1.1 1.1-2.3 2.8-2.3 4.5v10.2c0 2.3 1.1 4.5 3.4 5.1l5.6 2.3c6.8 2.3 15.3 5.6 16.4 7.9 1.7 2.8 2.8 12.4 2.8 20.9h-35.4z"/></svg>

            </div>
            <div class="menu-item__text">
              Groups
            </div>
          </a>
        </li>
      <li class="menu-item ic-app-header__menu-list-item ">
        <a id="global_nav_calendar_link" href="/calendar" class="ic-app-header__menu-list-link">
          <div class="menu-item-icon-container" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--calendar" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M197.07,213.38h16.31V197.07H197.07Zm-16.31,16.31V180.76h48.92v48.92Zm-48.92-16.31h16.31V197.07H131.85Zm-16.31,16.31V180.76h48.92v48.92ZM66.62,213.38H82.93V197.07H66.62ZM50.32,229.68V180.76H99.24v48.92Zm146.75-81.53h16.31V131.85H197.07Zm-16.31,16.31V115.54h48.92v48.92Zm-48.92-16.31h16.31V131.85H131.85Zm-16.31,16.31V115.54h48.92v48.92ZM66.62,148.15H82.93V131.85H66.62ZM50.32,164.46V115.54H99.24v48.92ZM34,262.29H246V82.93H34ZM246,66.62V42.16A8.17,8.17,0,0,0,237.84,34H213.38v8.15a8.15,8.15,0,1,1-16.31,0V34H82.93v8.15a8.15,8.15,0,0,1-16.31,0V34H42.16A8.17,8.17,0,0,0,34,42.16V66.62Zm-8.15-48.92a24.49,24.49,0,0,1,24.46,24.46V278.6H17.71V42.16A24.49,24.49,0,0,1,42.16,17.71H66.62V9.55a8.15,8.15,0,0,1,16.31,0v8.15H197.07V9.55a8.15,8.15,0,1,1,16.31,0v8.15Z"/></svg>

          </div>
          <div class="menu-item__text">
            Calendar
          </div>
        </a>
      </li>
      <li class="menu-item ic-app-header__menu-list-item ">
      <!-- TODO: Add back global search when available -->
        <a id="global_nav_conversations_link" href="/conversations" class="ic-app-header__menu-list-link">
          <div class="menu-item-icon-container">
            <span aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--inbox" version="1.1" x="0" y="0" viewBox="0 0 280 280" enable-background="new 0 0 280 280" xml:space="preserve"><path d="M91.72,120.75h96.56V104.65H91.72Zm0,48.28h80.47V152.94H91.72Zm0-96.56h80.47V56.37H91.72Zm160.94,34.88H228.52V10.78h-177v96.56H27.34A24.17,24.17,0,0,0,3.2,131.48V244.14a24.17,24.17,0,0,0,24.14,24.14H252.66a24.17,24.17,0,0,0,24.14-24.14V131.48A24.17,24.17,0,0,0,252.66,107.34Zm0,16.09a8.06,8.06,0,0,1,8,8v51.77l-32.19,19.31V123.44ZM67.58,203.91v-177H212.42v177ZM27.34,123.44H51.48v79.13L19.29,183.26V131.48A8.06,8.06,0,0,1,27.34,123.44ZM252.66,252.19H27.34a8.06,8.06,0,0,1-8-8V202l30,18H230.75l30-18v42.12A8.06,8.06,0,0,1,252.66,252.19Z"/></svg>
</span>
            <span class="menu-item__badge"></span>
          </div>
          <div class="menu-item__text">
            Inbox
          </div>
        </a>
      </li>
        <li class="menu-item ic-app-header__menu-list-item" >
          <a id="global_nav_history_link" role="button" href="#" class="ic-app-header__menu-list-link">
            <div class="menu-item-icon-container" aria-hidden="true">
              <svg viewBox="0 0 1920 1920" class="ic-icon-svg menu-item__icon svg-icon-history" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <path d="M960 112.941c-467.125 0-847.059 379.934-847.059 847.059 0 467.125 379.934 847.059 847.059 847.059 467.125 0 847.059-379.934 847.059-847.059 0-467.125-379.934-847.059-847.059-847.059M960 1920C430.645 1920 0 1489.355 0 960S430.645 0 960 0s960 430.645 960 960-430.645 960-960 960m417.905-575.955L903.552 988.28V395.34h112.941v536.47l429.177 321.77-67.765 90.465z" stroke="none" stroke-width="1" fill-rule="evenodd"/>
</svg>
            </div>
            <div class="menu-item__text">
              History
            </div>
          </a>
        </li>
        
    <li id="context_external_tool_144_menu_item" class="globalNavExternalTool menu-item ic-app-header__menu-list-item">
      <a class='ic-app-header__menu-list-link' href="/accounts/1/external_tools/144?launch_type=global_navigation">
          <img src="https://cdnsecakmi.kaltura.com/content/static/canvas/my_media.png" alt="Kaltura LTI" class="lti_tool_icon_large"/>
        <div class="menu-item__text">
          My Media
        </div>
      </a>
    </li>

      <li class="ic-app-header__menu-list-item">
        <a id="global_nav_help_link" role="button" class="ic-app-header__menu-list-link" data-track-category="help system" data-track-label="help button" href="https://help.instructure.com">
          <div class="menu-item-icon-container" role="presentation">
              <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg menu-item__icon svg-icon-help" version="1.1" x="0" y="0" viewBox="0 0 200 200" enable-background="new 0 0 200 200" xml:space="preserve" fill="currentColor"><path d="M100,127.88A11.15,11.15,0,1,0,111.16,139,11.16,11.16,0,0,0,100,127.88Zm8.82-88.08a33.19,33.19,0,0,1,23.5,23.5,33.54,33.54,0,0,1-24,41.23,3.4,3.4,0,0,0-2.74,3.15v9.06H94.42v-9.06a14.57,14.57,0,0,1,11.13-14,22.43,22.43,0,0,0,13.66-10.27,22.73,22.73,0,0,0,2.31-17.37A21.92,21.92,0,0,0,106,50.59a22.67,22.67,0,0,0-19.68,3.88,22.18,22.18,0,0,0-8.65,17.64H66.54a33.25,33.25,0,0,1,13-26.47A33.72,33.72,0,0,1,108.82,39.8ZM100,5.2A94.8,94.8,0,1,0,194.8,100,94.91,94.91,0,0,0,100,5.2m0,178.45A83.65,83.65,0,1,1,183.65,100,83.73,83.73,0,0,1,100,183.65" transform="translate(-5.2 -5.2)"/></svg>

            <span class="menu-item__badge"></span>
          </div>
          <div class="menu-item__text">
            Help
          </div>
</a>      </li>
    </ul>
  </div>
  <div class="ic-app-header__secondary-navigation">
    <ul class="ic-app-header__menu-list">
      <li class="menu-item ic-app-header__menu-list-item">
        <a
          id="primaryNavToggle"
          role="button"
          href="#"
          class="ic-app-header__menu-list-link ic-app-header__menu-list-link--nav-toggle"
          aria-label="Minimize global navigation"
          title="Minimize global navigation"
        >
          <div class="menu-item-icon-container" aria-hidden="true">
            <svg xmlns="http://www.w3.org/2000/svg" class="ic-icon-svg ic-icon-svg--navtoggle" version="1.1" x="0" y="0" width="40" height="32" viewBox="0 0 40 32" xml:space="preserve">
  <path d="M39.5,30.28V2.48H37.18v27.8Zm-4.93-13.9L22.17,4,20.53,5.61l9.61,9.61H.5v2.31H30.14l-9.61,9.61,1.64,1.64Z"/>
</svg>

          </div>
        </a>
      </li>
    </ul>
  </div>
  <div id="global_nav_tray_container"></div>
  <div id="global_nav_tour"></div>
</header>


  <div id="instructure_ajax_error_box">
    <div style="text-align: right; background-color: #fff;"><a href="#" class="close_instructure_ajax_error_box_link">Close</a></div>
    <iframe id="instructure_ajax_error_result" src="about:blank" style="border: 0;" title="Error"></iframe>
  </div>

  <div id="wrapper" class="ic-Layout-wrapper">
    <div id="main" class="ic-Layout-columns">
        <div class="ic-Layout-watermark"></div>
      <div id="not_right_side" class="ic-app-main-content">
        <div id="content-wrapper" class="ic-Layout-contentWrapper">
          
          <div id="content" class="ic-Layout-contentMain" role="main" aria-label="Global Content">
            




<div id="dashboard" class="ic-dashboard-app">
  <h1 class="screenreader-only">Dashboard</h1>
  
  
<div id='announcementWrapper'>
  
</div>








    <div id="dashboard_header_container" class="ic-Dashboard-header" data-props="null"></div>
      <div id="dashboard-planner" class="StudentPlanner__Container" style="display: none"></div>
    <div
      id="dashboard-activity"
      class="ic-Dashboard-Activity"
      style="display: none"
    >
      <!-- this will be populated via xhr from UsersController::dashboard_stream_items when someone selects the stream-items dashboard option -->
    </div>

          <script>
//<![CDATA[
(window.prefetched_xhrs = (window.prefetched_xhrs || {}))["/api/v1/dashboard/dashboard_cards"] = fetch("/api/v1/dashboard/dashboard_cards", {"credentials":"same-origin","headers":{"Accept":"application/json+canvas-string-ids, application/json","X-Requested-With":"XMLHttpRequest"}})
//]]>
</script>
    <script>
//<![CDATA[
(window.prefetched_xhrs = (window.prefetched_xhrs || {}))["/dashboard-sidebar"] = fetch("/dashboard-sidebar", {"credentials":"same-origin","headers":{"Accept":"application/json+canvas-string-ids, application/json","X-Requested-With":"XMLHttpRequest"}})
//]]>
</script>
<div id="DashboardCard_Container" style="display: block">
  <div class="ic-DashboardCard__box">
      <div class="ic-DashboardCard">
        <svg xmlns="http://www.w3.org/2000/svg" class="ic-DashboardCard__placeholder-svg" version="1.1" x="0" y="0" viewBox="-1087 618 260 254" xml:space="preserve">
          <title>Empty Card</title>
          <g class="ic-DashboardCard__placeholder-animates">
            <path d="M-1087 618h260v126h-260V618z"/>
            <rect x="-1062" y="759.5" class="st0" width="184" height="16"/>
            <rect x="-1062" y="785.5" class="st0" width="106" height="9"/>
            <circle cx="-1054" cy="842.5" r="8"/>
            <circle cx="-989" cy="842.5" r="8"/>
            <circle cx="-924" cy="842.5" r="8"/>
            <circle cx="-859" cy="842.5" r="8"/>
          </g>
        </svg>
      </div>
      <div class="ic-DashboardCard">
        <svg xmlns="http://www.w3.org/2000/svg" class="ic-DashboardCard__placeholder-svg" version="1.1" x="0" y="0" viewBox="-1087 618 260 254" xml:space="preserve">
          <title>Empty Card</title>
          <g class="ic-DashboardCard__placeholder-animates">
            <path d="M-1087 618h260v126h-260V618z"/>
            <rect x="-1062" y="759.5" class="st0" width="184" height="16"/>
            <rect x="-1062" y="785.5" class="st0" width="106" height="9"/>
            <circle cx="-1054" cy="842.5" r="8"/>
            <circle cx="-989" cy="842.5" r="8"/>
            <circle cx="-924" cy="842.5" r="8"/>
            <circle cx="-859" cy="842.5" r="8"/>
          </g>
        </svg>
      </div>
      <div class="ic-DashboardCard">
        <svg xmlns="http://www.w3.org/2000/svg" class="ic-DashboardCard__placeholder-svg" version="1.1" x="0" y="0" viewBox="-1087 618 260 254" xml:space="preserve">
          <title>Empty Card</title>
          <g class="ic-DashboardCard__placeholder-animates">
            <path d="M-1087 618h260v126h-260V618z"/>
            <rect x="-1062" y="759.5" class="st0" width="184" height="16"/>
            <rect x="-1062" y="785.5" class="st0" width="106" height="9"/>
            <circle cx="-1054" cy="842.5" r="8"/>
            <circle cx="-989" cy="842.5" r="8"/>
            <circle cx="-924" cy="842.5" r="8"/>
            <circle cx="-859" cy="842.5" r="8"/>
          </g>
        </svg>
      </div>
      <div class="ic-DashboardCard">
        <svg xmlns="http://www.w3.org/2000/svg" class="ic-DashboardCard__placeholder-svg" version="1.1" x="0" y="0" viewBox="-1087 618 260 254" xml:space="preserve">
          <title>Empty Card</title>
          <g class="ic-DashboardCard__placeholder-animates">
            <path d="M-1087 618h260v126h-260V618z"/>
            <rect x="-1062" y="759.5" class="st0" width="184" height="16"/>
            <rect x="-1062" y="785.5" class="st0" width="106" height="9"/>
            <circle cx="-1054" cy="842.5" r="8"/>
            <circle cx="-989" cy="842.5" r="8"/>
            <circle cx="-924" cy="842.5" r="8"/>
            <circle cx="-859" cy="842.5" r="8"/>
          </g>
        </svg>
      </div>
    <br/>
  </div>

</div>

</div>

          </div>
        </div>
        <div id="right-side-wrapper" class="ic-app-main-content__secondary">
          <aside id="right-side" role="complementary">
                <div class="placeholder"></div>

          </aside>
        </div>
      </div>
    </div>
      
<footer role="contentinfo" id="footer" class="ic-app-footer">
  <a href="http://www.instructure.com" class="footer-logo ic-app-footer__logo-link">
    <span class="screenreader-only">
      By Instructure
    </span>
  </a>
  <div id="footer-links" class="ic-app-footer__links">
    <a href="https://canvas.ku.edu/privacy_policy">Privacy Policy</a>
<a href="https://www.instructure.com/policies/canvas-lms-cookie-notice">Cookie Notice</a>
  <span
    id="terms_of_service_footer_link"
    class="
      terms_of_service_link terms_of_service_footer_link terms-of-service__link
    "
  ></span>
<a href="http://facebook.com/instructure">Facebook</a>
<a href="http://twitter.com/instructure">X.com</a>

  </div>
</footer>

  </div>



    <div style="display:none;"><!-- Everything inside of this should always stay hidden -->
        <div id="page_view_id">a20b208a-ef80-4581-a79d-9a34c418be75</div>
    </div>
  <div id='aria_alerts' class='hide-text affix' role="alert" aria-live="assertive"></div>
  <div id='StudentTray__Container'></div>
    <div class="NewUserTutorialTray__Container"></div>
  <div id="react-router-portals"></div>
  

  <iframe src="https://sso.canvaslms.com/post_message_forwarding?rev=59677caad5-de8233d392aa15f4&amp;token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJwYXJlbnRfZG9tYWluIjoiY2FudmFzLmt1LmVkdSJ9.NYVsCu6RI00SZPGIGtAWp2dsZPztIs5EqEF640ccZmszGe2eoLakG7-Bk3No0y_m0VFklEx5mH6IJU0F8xDjaw" name="post_message_forwarding" title="post_message_forwarding" id="post_message_forwarding" sandbox="allow-scripts allow-same-origin" style="display:none;"></iframe>


  <script>
    Object.assign(
      ENV,
      {}
    )
  </script>

<script>
//<![CDATA[
(window.bundles || (window.bundles = [])).push('nav_tourpoints');
(window.bundles || (window.bundles = [])).push('terms_of_service_modal');
(window.bundles || (window.bundles = [])).push('inst_fs_service_worker');
//]]>
</script>
<script src="https://instructure-uploads.s3.amazonaws.com/account_191320000000000001/attachments/13062279/UniversityofKansasCanvasCustomJSProductionFeb072025.js" defer="defer"></script>


</div> <!-- #application -->
</body>
</html>
"""
