Summary:	Common macros useful for building gnome packages
Summary(pl):	Wsp�lne makra przydatne do budowania pakiet�w GNOME
Name:		gnome-common
Version:	1.2.4
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnome.org/pub/gnome/pre-gnome2/sources/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnome-common provides macros for GNOME modules.

%description -l pl
Ten pakiet dostarcza makra do budowania pakiet�w GNOME.

%prep
%setup -q

%build
%configure --build=%{_build}

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
