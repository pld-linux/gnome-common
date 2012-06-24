Summary:	Common macros useful for building GNOME packages
Summary(es):	Macros comunes �tiles para construir paquetes de GNOME
Summary(pl):	Wsp�lne makra przydatne do budowania pakiet�w GNOME
Name:		gnome-common
Version:	2.4.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	9f5163e616b2a02af633de9c82557fa0
Patch0:		%{name}-am-1.7.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	autoconf >= 2.53
Requires:	automake >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l es
gnome-common provee unos macros para los m�dulos de GNOME.

%description -l pl
Ten pakiet dostarcza makra do budowania pakiet�w GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--build=%{_build}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/gnome-macros
%{_aclocaldir}/gnome2-macros
%{_datadir}/%{name}
