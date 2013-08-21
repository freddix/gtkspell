Summary:	GTK+ Spell Checker Interface Library
Name:		gtkspell
Version:	2.0.16
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://gtkspell.sourceforge.net/download/%{name}-%{version}.tar.gz
# Source0-md5:	f75dcc9338f182c571b321d37c606a94
Patch0:		%{name}-pc.patch
URL:		http://gtkspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd42-xml
BuildRequires:	enchant-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkSpell provides MSWord/MacOSX-style highlighting of misspelled words
in a GtkTextView widget. Right-clicking a misspelled word pops up a
menu of suggested replacements.

%package devel
Summary:	Header files for gtkspell
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for gtkspell.

%package apidocs
Summary:	gtkspell API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gtkspell API documentation.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/%{name}-2.0
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

