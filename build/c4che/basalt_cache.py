AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'basalt'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'basalt'
BUNDLE_NAME = 'Fade-2-Gray.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'darwin'
INCLUDES = ['basalt']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'gitHead': u'62f033719859a0b18aacec0eae66fc6f804cbdaf', u'_location': u'/pebble-clay', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.2.tgz', u'shasum': u'ed9f4e38f47650949969ec1a524b46a4cfee6d5b'}, u'_spec': u'pebble-clay@^1.0.1', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-clay-1.0.2.tgz_1468019683886_0.3709721537306905', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'pebble', u'config', u'configuration', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'_from': u'pebble-clay@>=1.0.1 <2.0.0', u'pebble': {u'sdkVersion': u'3', u'capabilities': [u'configurable'], u'projectType': u'package', u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'resources': {u'media': []}}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[{u'name': u'pebble-clay', u'escapedName': u'pebble-clay', u'rawSpec': u'^1.0.1', u'raw': u'pebble-clay@^1.0.1', u'scope': None, u'type': u'range', u'spec': u'>=1.0.1 <2.0.0'}, u'/Users/teodorescuandrei/gits/Fade-2-Gray']], u'_nodeVersion': u'6.2.1', u'version': u'1.0.2', u'_resolved': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.2.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/clay#readme', u'_npmVersion': u'3.9.3', u'_requested': {u'name': u'pebble-clay', u'escapedName': u'pebble-clay', u'rawSpec': u'^1.0.1', u'raw': u'pebble-clay@^1.0.1', u'scope': None, u'type': u'range', u'spec': u'>=1.0.1 <2.0.0'}, u'description': u'Pebble Config Framework', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)', u'lint': u'eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean'}, 'path': 'node_modules/pebble-clay/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-clay', u'license': u'MIT', u'directories': {}, u'author': {u'name': u'Pebble Technology'}, u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, u'_npmUser': {u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}, 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'_where': u'/Users/teodorescuandrei/gits/Fade-2-Gray', u'_id': u'pebble-clay@1.0.2', u'_shasum': u'ed9f4e38f47650949969ec1a524b46a4cfee6d5b'}]
LIB_RESOURCES_JSON = {u'pebble-clay': {}}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'TEMPERATURE': 10000, u'BACKGROUND_ON': 10005, u'WEATHER_SAFEMODE': 10007, u'WEATHER_ON': 10004, u'UNITS': 10001, u'ICON': 10002, u'BACKGROUND_COLOR': 10003, u'LOCATION': 10006}
MESSAGE_KEYS_DEFINITION = '/Users/teodorescuandrei/gits/Fade-2-Gray/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/Users/teodorescuandrei/gits/Fade-2-Gray/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/Users/teodorescuandrei/gits/Fade-2-Gray/build/js/message_keys.json'
PEBBLE_SDK_COMMON = '/Users/teodorescuandrei/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/Users/teodorescuandrei/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble/basalt'
PEBBLE_SDK_ROOT = '/Users/teodorescuandrei/Library/Application Support/Pebble SDK/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['basalt', 'color', 'rect'], 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'basalt', 'BUNDLE_BIN_DIR': 'basalt', 'BUILD_DIR': 'basalt', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH']}
PLATFORM_NAME = 'basalt'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'TEMPERATURE': 10000, u'BACKGROUND_ON': 10005, u'WEATHER_SAFEMODE': 10007, u'WEATHER_ON': 10004, u'UNITS': 10001, u'ICON': 10002, u'BACKGROUND_COLOR': 10003, u'LOCATION': 10006}, u'sdkVersion': u'3', u'projectType': u'native', u'uuid': u'0508f145-4275-4d9b-8f5c-918c73594637', u'messageKeys': {u'TEMPERATURE': 10000, u'BACKGROUND_ON': 10005, u'WEATHER_SAFEMODE': 10007, u'WEATHER_ON': 10004, u'UNITS': 10001, u'ICON': 10002, u'BACKGROUND_COLOR': 10003, u'LOCATION': 10006}, 'companyName': u'twaider', u'enableMultiJS': True, u'targetPlatforms': [u'aplite', u'basalt', u'chalk'], u'capabilities': [u'location', u'configurable'], 'versionLabel': u'1.0', 'longName': u'Fade 2 Gray', u'displayName': u'Fade 2 Gray', 'shortName': u'Fade 2 Gray', u'watchapp': {u'watchface': True}, u'resources': {u'media': [{u'type': u'png', u'menuIcon': True, u'targetPlatforms': None, u'name': u'IMAGE_MENU', u'file': u'images/ks_menu.png'}, {u'type': u'font', u'targetPlatforms': None, u'characterRegex': u'[0-9:]', u'name': u'FONT_PIXEL_MIL_52', u'file': u'fonts/pixelmil'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_PIXEL_MIL_24', u'file': u'fonts/pixelmil'}, {u'type': u'font', u'targetPlatforms': None, u'characterRegex': u'[0-9:\xb0a-izA-IZ\\-]', u'name': u'FONT_NUPE_23', u'file': u'fonts/nupe.ttf'}]}, 'name': u'fade-to-gray'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk']
RESOURCES_JSON = [{u'type': u'png', u'menuIcon': True, u'targetPlatforms': None, u'name': u'IMAGE_MENU', u'file': u'images/ks_menu.png'}, {u'type': u'font', u'targetPlatforms': None, u'characterRegex': u'[0-9:]', u'name': u'FONT_PIXEL_MIL_52', u'file': u'fonts/pixelmil'}, {u'targetPlatforms': None, u'type': u'font', u'name': u'FONT_PIXEL_MIL_24', u'file': u'fonts/pixelmil'}, {u'type': u'font', u'targetPlatforms': None, u'characterRegex': u'[0-9:\xb0a-izA-IZ\\-]', u'name': u'FONT_NUPE_23', u'file': u'fonts/nupe.ttf'}]
RPATH_ST = '-Wl,-rpath,%s'
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 79
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk']
TARGET_PLATFORMS = ['chalk', 'basalt', 'aplite']
TIMESTAMP = 1469171690
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
