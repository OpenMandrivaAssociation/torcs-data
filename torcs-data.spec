%define	pname	torcs
%define	opname	TORCS
%define	name	%{pname}-data
%define	oname	%{opname}-data
%define	version	1.3.0
%define	release	1
%define	Summary	Data files for %{pname}

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
Source0:	%{opname}-%{version}-data.tar.bz2
Source1:	%{opname}-%{version}-data-tracks-road.tar.bz2
Source2:	%{opname}-%{version}-data-tracks-oval.tar.bz2
Source3:	%{opname}-%{version}-data-tracks-dirt.tar.bz2
Source4:	%{opname}-%{version}-data-cars-extra.tar.bz2
Source5:	%{opname}-%{version}-data-cars-nascar.tar.bz2
Source6:	%{opname}-%{version}-data-cars-Patwo-Design.tar.bz2
Source7:	%{opname}-%{version}-data-cars-kcendra-gt.tar.bz2
Source8:	%{opname}-%{version}-data-cars-kcendra-roadsters.tar.bz2
Source9:	%{opname}-%{version}-data-cars-kcendra-sport.tar.bz2
Source10:	%{opname}-%{version}-data-cars-VM.tar.bz2
Url:		http://torcs.org/
BuildArch:	noarch
Requires:	%{pname} = %{version}

%description
%{Summary}

%package cars-extra
Group:		Games/Arcade
Requires:	%{name} >= %{version}
Summary:	Extra cars for %{opname}
Obsoletes:	%{name}-cars-Patwo-Design
Provides:	%{name}-cars-Patwo-Design

%description cars-extra
Extra cars for %{opname}

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE0} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE1} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE2} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE3} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE4} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE5} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE6} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE7} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE8} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE9} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}
%{__tar} -jxf %{SOURCE10} -C $RPM_BUILD_ROOT%{_gamesdatadir}/%{pname}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%dir %{_gamesdatadir}/%{pname}/cars
%{_gamesdatadir}/%{pname}/cars/360-modena/
%{_gamesdatadir}/%{pname}/cars/car1-trb1/
%{_gamesdatadir}/%{pname}/categories
%{_gamesdatadir}/%{pname}/data
%{_gamesdatadir}/%{pname}/menu
%{_gamesdatadir}/%{pname}/tracks

%files cars-extra
%defattr(-,root,root,755)
%{_gamesdatadir}/%{pname}/cars/155-DTM
%{_gamesdatadir}/%{pname}/cars/acura-nsx-sz
%{_gamesdatadir}/%{pname}/cars/baja-bug
%{_gamesdatadir}/%{pname}/cars/buggy
%{_gamesdatadir}/%{pname}/cars/cg-nascar-rwd
%{_gamesdatadir}/%{pname}/cars/clkdtm
%{_gamesdatadir}/%{pname}/cars/gt40
%{_gamesdatadir}/%{pname}/cars/lotus-gt1
%{_gamesdatadir}/%{pname}/cars/mclaren-f1
%{_gamesdatadir}/%{pname}/cars/porsche-gt1
%{_gamesdatadir}/%{pname}/cars/porsche-gt3rs
%{_gamesdatadir}/%{pname}/cars/viper-gts-r
%{_gamesdatadir}/%{pname}/cars/xj-220
%{_gamesdatadir}/%{pname}/cars/kc-*
%{_gamesdatadir}/%{pname}/cars/p406
%{_gamesdatadir}/%{pname}/cars/pw-*
%{_gamesdatadir}/%{pname}/cars/vm-x*
%{_gamesdatadir}/%{pname}/cars/sc-f1


