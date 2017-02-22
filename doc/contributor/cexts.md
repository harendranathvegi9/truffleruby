# TruffleRuby, Sulong and C extensions

TruffleRuby runs C extension using Sulong. You should build Sulong from source.
Set `SULONG_VERSION=3.2` when building.

https://github.com/graalvm/sulong

Then set `SULONG_HOME` environment variables to the Sulong repository.

```
$ export SULONG_HOME=.../sulong
```

You need LLVM installed. Version 3.3 seems to work best (3.2, which is the
compatibility we've set, isn't available easily on macOS). You can set
`JT_CLANG` and `JT_OPT` to those binaries if you need to use a non-system
version.

You can now build the C extension support. Building the OpenSSL C extension is
incomplete, so most people probably want to disable that.

```
$ jt build cexts --no-openssl
```

Get the `jruby-truffle-gem-test-pack` repository.

https://github.com/jruby/jruby-truffle-gem-test-pack

You can then test C extension support.

```
$ export GEM_HOME=../jruby-truffle-gem-test-pack/gems
$ jt test cexts --no-libxml --no-openssl
```

If you want to test `libxml`, remove that flag and set either `LIBXML_HOME` or
`LIBXML_INCLUDE` and `LIBXML_LIB`. Try the same with `OPENSSL_` if you are
adventurous.

You can also runs specs:

```
$ jt test --sulong :capi
```

To run C extension benchmarks, you first need to compile them.

```
$ jt cextc .../all-ruby-benchmarks/chunky_png/oily_png/
```

Then follow the instructions for benchmarking above, and then try:

```
$  USE_CEXTS=true TRUFFLERUBYOPT=-Xcexts.log.load=true jt benchmark .../all-ruby-benchmarks/chunky_png/chunky-color-r.rb --simple
```

These benchmarks have Ruby fallbacks, so we should carefully check that the
C extension is actually being used by looking for these log lines.

```
[ruby] INFO loading cext module ...
```
