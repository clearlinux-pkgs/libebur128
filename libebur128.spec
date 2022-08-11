#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libebur128
Version  : 1.2.6
Release  : 5
URL      : https://github.com/jiixyj/libebur128/archive/v1.2.6/libebur128-1.2.6.tar.gz
Source0  : https://github.com/jiixyj/libebur128/archive/v1.2.6/libebur128-1.2.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libebur128-lib = %{version}-%{release}
Requires: libebur128-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : pkg-config

%description
libebur128
==========
libebur128 is a library that implements the EBU R 128 standard for loudness
normalisation.

%package dev
Summary: dev components for the libebur128 package.
Group: Development
Requires: libebur128-lib = %{version}-%{release}
Provides: libebur128-devel = %{version}-%{release}
Requires: libebur128 = %{version}-%{release}

%description dev
dev components for the libebur128 package.


%package lib
Summary: lib components for the libebur128 package.
Group: Libraries
Requires: libebur128-license = %{version}-%{release}

%description lib
lib components for the libebur128 package.


%package license
Summary: license components for the libebur128 package.
Group: Default

%description license
license components for the libebur128 package.


%prep
%setup -q -n libebur128-1.2.6
cd %{_builddir}/libebur128-1.2.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656129647
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -ffat-lto-objects -flto=auto -march=x86-64-v3 -msse2avx -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1656129647
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libebur128
cp %{_builddir}/libebur128-1.2.6/COPYING %{buildroot}/usr/share/package-licenses/libebur128/2627ff03833f74ed51a7f43c55d30b249b6a0707
cp %{_builddir}/libebur128-1.2.6/doc/license/R128Scan.txt %{buildroot}/usr/share/package-licenses/libebur128/677e4a0f00605ca9e5d206c562652bfdf89b8456
cp %{_builddir}/libebur128-1.2.6/doc/license/queue.txt %{buildroot}/usr/share/package-licenses/libebur128/38d1b75e874a9f1e5e4a61e06953710f670a32fe
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ebur128.h
/usr/lib64/libebur128.so
/usr/lib64/pkgconfig/libebur128.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libebur128.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libebur128.so.1
/usr/lib64/glibc-hwcaps/x86-64-v3/libebur128.so.1.2.6
/usr/lib64/libebur128.so.1
/usr/lib64/libebur128.so.1.2.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libebur128/2627ff03833f74ed51a7f43c55d30b249b6a0707
/usr/share/package-licenses/libebur128/38d1b75e874a9f1e5e4a61e06953710f670a32fe
/usr/share/package-licenses/libebur128/677e4a0f00605ca9e5d206c562652bfdf89b8456
