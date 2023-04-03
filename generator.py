import os
from folders import *

main_dir = [base, features]
main_dir_names = ['base', 'features']
starter_path_features = "D:\\generator_ex\\example\\lib\\features"
# starter_path_features = "D:\\generator_ex\\example\\lib\\features"


def main():

    for i in range(0, len(main_dir)):
        for j in range(0, len(main_dir[i])):
            dirName = str(main_dir_names[i]) + '/' + str(main_dir[i][j])

            try:
                os.makedirs(dirName, exist_ok=True)
                if main_dir[i][j] == 'splash':

                    open(
                        starter_path_features+"\\splash\\splash_page.dart", "x")
                    open(
                        starter_path_features+"\\splash\\splash_animation.dart", "x")
                if main_dir[i][j] == 'home':

                    os.mkdir(
                        starter_path_features+"\\home\\widgets")
                    os.mkdir(
                        starter_path_features+"\\home\\pages")
                    home_page = open(
                        starter_path_features+"\\\home\\home_page.dart", "x")
                    home_page.write("import 'package:flutter/material.dart';")
                if main_dir[i][j] == 'auth':

                    os.mkdir(
                        starter_path_features+"\\auth\\widgets")
                    os.mkdir(
                        starter_path_features+"\\auth\\login")

                    os.mkdir(
                        starter_path_features+"\\auth\\signin")
                    login_page = open(
                        starter_path_features+"\\auth\\login\\login_page.dart", "x")
                    login_page.write("import 'package:flutter/material.dart';")
                    signin_page = open(
                        starter_path_features+"\\auth\\signin\\signin_page.dart", "x")
                    signin_page.write(
                        "import 'package:flutter/material.dart';")
                if main_dir[i][j] == 'l10n':
                    os.mkdir("D:\\generator_ex\\example\\lib\\base\\l10n\\arb")
                    localization = open(
                        "D:\\generator_ex\\example\\lib\\base\\l10n\\localization_helper.dart", "x")
                    localization.write(
                        "import 'package:flutter/widgets.dart';\n " +
                        "//DO: import and export \n" +
                        "/*extension AppLocalizationsX on BuildContext {\n AppLocalizations get l10n =>" +
                        "AppLocalizations.of(this)!;\n}*/"
                    )
                if main_dir[i][j] == 'app':
                    app = open(
                        "D:\\generator_ex\\example\\lib\\base\\app\\app_setup.dart", "x")
                    app.write(
"import 'package:flutter/rendering.dart';\n"+
"import 'dart:async';\n"+
"import 'package:flutter/services.dart';\n"+
"//import 'package:logging/logging.dart';\n"+
"import 'package:flutter/foundation.dart';\n"+
"import 'package:flutter/material.dart';\n"+
"import 'dart:isolate';\n\n"+
"//import 'package:firebase_core/firebase_core.dart';\n"+
"//import 'package:firebase_crashlytics/firebase_crashlytics.dart';\n\n"+
"/*Future<void> configureAppAndRun() async {\n"+
"  _disableLogs(disableLogs: kReleaseMode);\n"+
"  await _configureApp();\n"+
"  \n"+
"  await runZonedGuarded<Future<void>>(() async{\n"+
"     if (kDebugMode) {\n"+
"      //Log more in debug mode\n"+
"      Logger.root.level = Level.FINE;\n"+
"    }\n"+
"    if(kReleaseMode){\n"+
"      Logger.root.level=Level.WARNING;\n"+
"    }\n"+
"    //Subscribe to log message\n"+
"    Logger.root.onRecord.listen((record) {\n"+
"      final message = '${record.level.name}: ${record.time}: '\n"+
"          '${record.loggerName}: '\n"+
"          '${record.message}';\n"+
"\n"+
"      //FirebaseCrashlytics.instance.log(message);\n"+
"\n"+
"      /*if (record.level >= Level.SEVERE) {\n"+
"        FirebaseCrashlytics.instance.recordError(\n"+
"          message,\n"+
"          filterStackTrace(StackTrace.current),\n"+
"          fatal: true,\n"+
"        );\n"+
"      }*/\n"+
"    });\n"+
"  if(kDebugMode){\n"+
"    //enable in debug mode to test unnecessary repaints\n"+
"    //wrap animation with RepaintBoundary if needed\n"+
"    debugRepaintRainbowEnabled=true;\n"+
"    //highlight oversized images\n"+
"    debugInvertOversizedImages=true;\n"+
"  }\n"+
"  \n"+
"  \n"+
"  \n"+
"  runApp(const AppName());\n"+
"\n"+
"  }, (error, stack) { \n"+
"    debugPrint('ERROR: $error\n\n'\n"+
"        'STACK:$stack');\n"+
"    //FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);\n"+
"  });\n"+
"\n"+
"  \n"+
"}*/\n\n"+

                        "void _disableLogs({bool disableLogs = false}) {\n" +
                        "if (!disableLogs) return;\n" +
                        "debugPrint = (String? message, {int? wrapWidth}) {};\n" +
                        "}\n\n" +

                        "Future<void> _configureApp() async {\n" +
                        "  WidgetsFlutterBinding.ensureInitialized();\n" +
                        "  //await safeRun(()=>Firebase.initializeApp());\n" +
                        "  SystemChrome.setEnabledSystemUIMode(\n" +
                        "    SystemUiMode.edgeToEdge,\n" +
                        "  );\n" +
                        "\n" +
                        "  catchFatalFrameworkErrors();\n" +
                        "  catchFatalNonFrameworkErrors();\n" +
                        "  catchFatalErrorsOutsideFlutter();\n" +
                        "}\n\n" +


                        "void catchFatalFrameworkErrors() {\n" +
                        "FlutterError.onError = (errorDetails) {\n" +
                        "//FirebaseCrashlytics.instance.recordFlutterFatalError(errorDetails);\n" +
                        "};\n" +
                        "}\n" +
                        "\n" +
                        "void catchFatalNonFrameworkErrors() {\n" +
                        "  PlatformDispatcher.instance.onError = (error, stack) {\n" +
                        "   // FirebaseCrashlytics.instance.recordError(error, stack, fatal: true);\n" +
                        "    return true;\n" +
                        "  };\n" +
                        "}\n" +
                        "\n" +
                        "void catchFatalErrorsOutsideFlutter() {\n" +
                        "    // To catch errors outside of the Flutter context, we attach an error\n" +
                        "      // listener to the current isolate.\n" +
                        "  Isolate.current.addErrorListener(RawReceivePort((pair) async {\n" +
                        "    final List<dynamic> errorAndStacktrace = pair;\n" +
                        "    //await FirebaseCrashlytics.instance.recordError(\n" +
                        "      //errorAndStacktrace.first,\n" +
                        "      //errorAndStacktrace.last,\n" +
                        "     // fatal: true,\n" +
                        "     // printDetails: true,\n" +
                        "    //);\n" +
                        "  }).sendPort);\n" +
                        "}\n" +
                        "\n" +
                        "@visibleForTesting\n" +
                        "StackTrace filterStackTrace(StackTrace stackTrace) {\n" +
                        "  try {\n" +
                        "    final lines = stackTrace.toString().split(''\n'');\n" +
                        "    final buffer = StringBuffer();\n" +
                        "    for (final line in lines) {\n" +
                        "      if (line.contains('crashlytics.dart') ||\n" +
                        "          line.contains('_BroadcastStreamController.java') ||\n" +
                        "          line.contains('logger.dart')) {\n" +
                        "        continue;\n" +
                        "      }\n" +
                        "      buffer.writeln(line);\n" +
                        "    }\n" +
                        "    return StackTrace.fromString(buffer.toString());\n" +
                        "  } catch (e) {\n" +
                        "    debugPrint('Problem while filtering stack trace: $e');\n" +
                        "  }\n" +
                        "\n" +
                        "  // If there was an error while filtering,\n" +
                        "  // return the original, unfiltered stack track.\n" +
                        "  return stackTrace;\n" +
                        "\n}"

                    )
                if main_dir[i][j] == 'common_widgets':
                    app_scaffold = open(
                        "D:\\generator_ex\\example\\lib\\base\\common_widgets\\app_scaffold.dart", "x")
                    app_scaffold.write(
                        "import 'package:flutter/material.dart';\n")
                    app_scaffold.write(
                        "import 'package:flutter/services.dart';\n\n")
                    app_scaffold.write(
                        "class AppScaffold extends StatelessWidget {\n" +
                        "const AppScaffold({\nsuper.key,\nrequired this.child,\nthis.appBar,\n" +
                        "this.drawer,\n  this.resize,\n  this.extendBody,\n});\n\n" +
                        "final bool? resize;\n" +
                        "final bool? extendBody;\n" +
                        "final Widget child;\n" +
                        "final AppBar? appBar;\n" +
                        "final Drawer? drawer;\n\n" +
                        "@override\n Widget build(BuildContext context) {\n" +
                        "SystemChrome.setSystemUIOverlayStyle(\n const SystemUiOverlayStyle(\n" +
                        "systemNavigationBarColor: Colors.transparent,\n" +
                        "statusBarColor: Colors.transparent),\n);\n return Scaffold(\n" +
                        "extendBody: extendBody!,\nresizeToAvoidBottomInset: resize,\n" +
                        "drawerEnableOpenDragGesture: false,\nappBar: appBar,\n" +
                        "drawer: drawer,\n body: SafeArea(child: child),\n);\n}\n}" +
                        ""
                    )
                if main_dir[i][j] == 'routers':
                    open(
                        "D:\\generator_ex\\example\\lib\\base\\routers\\router.dart", "x")
                if main_dir[i][j] == 'theme':
                    open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\theme_provider.dart", "x")
                    os.mkdir(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme")
                    open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme\\app_theme.dart", "x")
                    colors = open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme\\app_colors.dart", "x")
                    colors.write("import 'package:flutter/material.dart';\n\n")
                    colors.write("class AppColors{\n}")
                    icons = open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme\\app_icons.dart", "x")
                    icons.write("import 'package:flutter/material.dart';\n\n")
                    icons.write(
                        "//example: static IconData get email => Icons.email\n")
                    icons.write("class AppIcons{\n}")
                    images = open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme\\app_images.dart", "x")
                    images.write("import 'package:flutter/material.dart';\n")
                    images.write("//import 'dart:io';")
                    images.write(
                        "//examples:\n// static final photo = Image.asset(path)\n")
                    images.write("// static final File photo = File(path)\n")
                    images.write("class AppImages{\n}")
                    typography = open(
                        "D:\\generator_ex\\example\\lib\\base\\theme\\app_theme\\app_typography.dart", "x")
                    typography.write(
                        "import 'package:flutter/material.dart';\n\n")
                    typography.write("class AppTypography{\n}")

                print("Directory ", dirName,  " Created ")
            except FileExistsError:
                print("Directory ", dirName,  " already exists")

            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory ", dirName,  " Created ")
            else:
                print("Directory ", dirName,  " already exists")


if __name__ == '__main__':
    main()
