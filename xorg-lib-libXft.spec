
#
Summary:	X Font Rendering library
Summary(pl):	Biblioteka do renderowania fontów
Name:		xorg-lib-libXft
Version:	2.1.7
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXft-%{version}.tar.bz2
# Source0-md5:	b5cf0ee9c60f842687d5606aa41a079d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
Obsoletes:	XFree86-xft
Obsoletes:	XFree86-xft2
Obsoletes:	Xft
Obsoletes:	libXft
Obsoletes:	xft
BuildRoot:	%{tmpdir}/libXft-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xft is a font rendering library for X.

%description -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.


%package devel
Summary:	Header files libXft development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXft
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXft = %{version}-%{release}
Requires:	fontconfig-devel
Requires:	xorg-lib-libXrender-devel
Obsoletes:	XFree86-xft-devel
Obsoletes:	XFree86-xft2-devel
Obsoletes:	Xft-devel
Obsoletes:	libXft-devel
Obsoletes:	xft-devel

%description devel
Xft is a font rendering library for X.

This package contains the header files needed to develop programs that
use these libXft.

%description devel -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXft.


%package static
Summary:	Static libXft libraries
Summary(pl):	Biblioteki statyczne libXft
Group:		Development/Libraries
Requires:	xorg-lib-libXft-devel = %{version}-%{release}
Obsoletes:	XFree86-xft-static
Obsoletes:	Xft-static
Obsoletes:	libXft-static
Obsoletes:	xft-static

%description static
Xft is a font rendering library for X.

This package contains the static libXft library.

%description static -l pl
Xft jest bibliotek± s³u¿±c± do renderowania fontów dla X Window.

Pakiet zawiera statyczn± bibliotekê libXft.


%prep
%setup -q -n libXft-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,wheel) %{_libdir}/libXft.so.*


%files devel
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/xft-config
%{_includedir}/X11/Xft/*.h
%{_libdir}/libXft.la
%attr(755,root,wheel) %{_libdir}/libXft.so
%{_pkgconfigdir}/xft.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXft.a
