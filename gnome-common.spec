Summary:	Common macros useful for building GNOME packages
Summary(es.UTF-8):	Macros comunes útiles para construir paquetes de GNOME
Summary(pl.UTF-8):	Wspólne makra przydatne do budowania pakietów GNOME
Name:		gnome-common
Version:	3.4.0.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-common/3.4/%{name}-%{version}.tar.xz
# Source0-md5:	18480be01c632577002462054062c42b
Patch0:		%{name}-omf.patch
Patch1:		%{name}-docdir.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	autoconf >= 2.53
Requires:	automake >= 1:1.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l es.UTF-8
gnome-common provee unos macros para los módulos de GNOME.

%description -l pl.UTF-8
Ten pakiet dostarcza makra do budowania pakietów GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
%attr(755,root,root) %{_bindir}/gnome-autogen.sh
%attr(755,root,root) %{_bindir}/gnome-doc-common
%{_aclocaldir}/gnome-common.m4
%{_aclocaldir}/gnome-compiler-flags.m4
%{_datadir}/gnome-common
