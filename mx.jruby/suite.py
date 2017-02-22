# Copyright (c) 2016 Oracle and/or its affiliates. All rights reserved. This
# code is released under a tri EPL/GPL/LGPL license. You can use it,
# redistribute it and/or modify it under the terms of the:
#
# Eclipse Public License version 1.0
# GNU General Public License version 2
# GNU Lesser General Public License version 2.1

def mavenLib(mavenDep, sha1, sourceSha1, mavenLibLicense):
    components = mavenDep.split(':')
    if len(components) == 3:
        groupId, artifactId, version = components
        native = None
    else:
        groupId, artifactId, version, native = components
    if native:
        args = (groupId.replace('.', '/'), artifactId, version, artifactId, version, native)
        base = "https://search.maven.org/remotecontent?filepath=%s/%s/%s/%s-%s-%s" % args
    else:
        args = (groupId.replace('.', '/'), artifactId, version, artifactId, version)
        base = "https://search.maven.org/remotecontent?filepath=%s/%s/%s/%s-%s" % args
    url = base + ".jar"
    sourceUrl = base + '-sources.jar'
    description = {
        "urls": [url],
        "sha1": sha1,
        "maven": {
            "groupId": groupId,
            "artifactId": artifactId,
            "version": version,
        },
        "license": mavenLibLicense
    }
    if sourceSha1:
        description["sourceUrls"] = [sourceUrl]
        description["sourceSha1"] = sourceSha1
    return description

suite = {
    "mxversion": "5.59.0",
    "name": "jrubytruffle",

    "imports": {
        "suites": [
            {
                "name": "truffle",
                # Must be the same as in truffle/pom.rb (except for the -SNAPSHOT part only in pom.rb, and there we can use a release name)
                "version": "bedd07ffe41330aaf4cb50c2a8a38b0af95545b4",
                "urls": [
                    {"url": "https://github.com/graalvm/truffle.git", "kind": "git"},
                    {"url": "https://curio.ssw.jku.at/nexus/content/repositories/snapshots", "kind": "binary"},
                ]
            },
        ],
    },

    "licenses": {
        "EPL-1.0": {
            "name": "Eclipse Public License 1.0",
            "url": "https://opensource.org/licenses/EPL-1.0",
        },
        "BSD-simplified" : {
          "name" : "Simplified BSD License (2-clause BSD license)",
          "url" : "http://opensource.org/licenses/BSD-2-Clause"
        },
        "MIT" : {
          "name" : "MIT License",
          "url" : "http://opensource.org/licenses/MIT"
        },
        "Apache-2.0" : {
          "name" : "Apache License 2.0",
          "url" : "https://opensource.org/licenses/Apache-2.0"
        },
        "GPLv2" : {
          "name" : "GNU General Public License, version 2",
          "url" : "http://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html"
        },
        "zlib" : {
          "name" : "The zlib License",
          "url" : "https://opensource.org/licenses/zlib"
        },
    },

    "repositories" : {
         "jruby-binary-snapshots" : {
             "url" : "https://curio.ssw.jku.at/nexus/content/repositories/snapshots",
             "licenses" : ["EPL-1.0", "BSD-simplified", "BSD-new", "MIT", "Apache-2.0", "GPLv2", "LGPLv21", "zlib"]
          },
     },

    "libraries": {

        # ------------- Libraries -------------

        "ASM": mavenLib(
          "org.ow2.asm:asm:5.0.4",
          "0da08b8cce7bbf903602a25a3a163ae252435795",
          "112ff54474f1f04ccf1384c92e39fdc566f0bb5e",
          "BSD-new"),

        "JNR_POSIX": mavenLib(
          "com.github.jnr:jnr-posix:3.0.34",
          "65744f1fc0b4520472f566b2a6e5f464246147d3",
          "673fb5780296a6328dcc014e734ee7be254b3020",
          "EPL-1.0"),

        "JNR_CONSTANTS": mavenLib(
          "com.github.jnr:jnr-constants:0.9.6",
          "84955256aa28919f12b6c7c9437ed65d814a3c0c",
          "5579ab41c687085e714fc330536ec4dda3350b08",
          "Apache-2.0"),

        "JNR_FFI": mavenLib(
          "com.github.jnr:jnr-ffi:2.1.3",
          "eae1dd4a7454ddbf000bb95f5c1912894221f5e1",
          "fcd823ddc2d1d17dca8ea63ba680d6c50f388e0b",
          "Apache-2.0"),

        "JFFI": mavenLib(
          "com.github.jnr:jffi:1.2.13",
          "8926bd0b2d0e9a46e7607eb7866356845c7df9a2",
          "691ec868b9569092687553a8099a28f71f175097",
          "Apache-2.0"),

        "JFFI_NATIVE": mavenLib(
          "com.github.jnr:jffi:1.2.13:native",
          "c4b81ddacd1e94a73780aa6e4e8b9d2945d5eb4c",
          None,
          ["Apache-2.0", "MIT"]),

        "SNAKEYAML": mavenLib(
            "org.yaml:snakeyaml:1.14",
            "c2df91929ed06a25001939929bff5120e0ea3fd4",
            "4c6bcedc3efa772a5ae1c2fd01efee8e4d15edac",
            "Apache-2.0"),

        "JONI": mavenLib(
            "org.jruby.joni:joni:2.1.11",
            "655cc3aba1bc9dbdd653f28937bec16f3e9c4cec",
            "2982d6beb2f8fabe5ac5cc9dec6b4d6a9ffeedb1",
            "MIT"),

        "JCODINGS": mavenLib(
            "org.jruby.jcodings:jcodings:1.0.18",
            "e2c76a19f00128bb1806207e2989139bfb45f49d",
            "201985f0f15af95f03494ab9ef0400e849090d6c",
            "MIT"),

    },

    "projects": {

        # ------------- Projects -------------

        "jruby-truffle": {
            "dir": "truffleruby/src/main",
            "sourceDirs": ["java"],
            "dependencies": [
                "truffle:TRUFFLE_API",
                "truffle:TRUFFLE_DEBUG",
                "truffle:JLINE",
                "ASM",
                "JNR_POSIX",
                "JNR_CONSTANTS",
                "JNR_FFI",
                "JFFI",
                "JFFI_NATIVE",
                "SNAKEYAML",
                "JONI",
                "JCODINGS",
            ],
            "annotationProcessors": ["truffle:TRUFFLE_DSL_PROCESSOR"],
            "javaCompliance": "1.8",
            "workingSets": "JRubyTruffle",
            "checkPackagePrefix": "false",
            "license": ["EPL-1.0", "BSD-new", "BSD-simplified", "MIT", "Apache-2.0"],
        },

        "jruby-truffle-ruby": {
            "class": "ArchiveProject",
            "outputDir": "truffleruby/src/main/ruby",
            "prefix": "truffleruby",
            "license": ["EPL-1.0", "BSD-new"],
        },

        "jruby-truffle-test": {
            "dir": "truffleruby/src/test",
            "sourceDirs": ["java"],
            "dependencies": [
                "jruby-truffle",
                "truffle:TRUFFLE_TCK",
                "mx:JUNIT",
            ],
            "javaCompliance": "1.8",
            "checkPackagePrefix": "false",
            "license": "EPL-1.0",
        },

        "jruby-truffle-ruby-test": {
            "class": "ArchiveProject",
            "outputDir": "truffleruby/src/test/ruby",
            "prefix": "src/test/ruby",
            "license": "EPL-1.0",
        },

        "jruby-lib-ruby": {
            "class": "ArchiveProject",
            "outputDir": "lib",
            "prefix": "lib",
            "license": ["EPL-1.0", "MIT", "BSD-simplified", "GPLv2", "LGPLv21", "zlib"],
        },

        "jruby-docs": {
            "class": "TruffleRubyDocsProject",
            "outputDir": "",
            "prefix": "",
        },
    },

    "distributions": {

        # ------------- Distributions -------------

        "RUBY": {
            "mainClass": "org.jruby.Main",
            "dependencies": [
                "jruby-truffle",
                "jruby-truffle-ruby",
            ],
            "distDependencies": [
                "truffle:TRUFFLE_API",
                "truffle:TRUFFLE_DEBUG",
            ],
            "description": "JRuby+Truffle",
            "license": ["EPL-1.0", "BSD-new", "BSD-simplified", "MIT", "Apache-2.0"],
        },

        # Set of extra files to extract to run Ruby
        "RUBY-ZIP": {
            "native": True, # Not Java
            "relpath": True,
            "dependencies": [
                "jruby-lib-ruby",
                "jruby-docs",
            ],
            "overlaps": [
                "RUBY",
            ],
            "description": "JRuby+Truffle Native Libs",
            "license": ["EPL-1.0", "MIT", "BSD-simplified", "GPLv2", "LGPLv21", "zlib"],
        },

        "RUBY-TEST": {
            "dependencies": [
                "jruby-truffle-test",
                "jruby-truffle-ruby-test",
            ],
            "exclude" : [
                "mx:HAMCREST",
                "mx:JUNIT"
            ],
            "distDependencies": [
                "RUBY",
                "truffle:TRUFFLE_TCK"
            ],
            "license": "EPL-1.0",
        },
    },
}
