
%define		snap		20030710

Summary:	Common macros useful for building gnome packages
Summary(pl):	Wspólne makra przydatne do budowania pakietów GNOME
Name:		gnome-common
Version:	2.3.0
Release:	0.%{snap}
License:	GPL
Group:		Development/Tools
#Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.2/%{name}-%{version}.tar.bz2
Source0:	%{name}-%{version}-%{snap}.tar.bz2
# Source0-md5:	1b50dc13f5249a32a5055df9382cf5c8
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Requires:	automake
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l pl
Ten pakiet dostarcza makra do budowania pakietów GNOME.

%prep
%setup -q

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
