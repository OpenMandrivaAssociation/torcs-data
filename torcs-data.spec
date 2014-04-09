%define	pname	torcs
%define	opname	TORCS
%define	name	%{pname}-data
%define	oname	%{opname}-data
%define	version	1.3.5
%define	release	1
%define	Summary	Data files for %{pname}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Arcade
Source0:	%{opname}-%{version}-data.tar.xz
Source1:	%{opname}-%{version}-data-tracks-road.tar.xz
Source2:	%{opname}-%{version}-data-tracks-oval.tar.xz
Source3:	%{opname}-%{version}-data-tracks-dirt.tar.xz
Source4:	%{opname}-%{version}-data-cars-extra.tar.xz
Source5:	%{opname}-1.3.0-data-cars-nascar.tar.bz2
Source6:	%{opname}-%{version}-data-cars-Patwo-Design.tar.xz
Source7:	%{opname}-%{version}-data-cars-kcendra-gt.tar.xz
Source8:	%{opname}-%{version}-data-cars-kcendra-roadsters.tar.xz
Source9:	%{opname}-%{version}-data-cars-kcendra-sport.tar.xz
Source10:	%{opname}-1.3.0-data-cars-VM.tar.bz2
Url:		http://torcs.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%exclude %{_gamesdatadir}/%{pname}/categories/Nascar.xml
%{_gamesdatadir}/%{pname}/categories/*
%{_gamesdatadir}/%{pname}/data/*
%{_gamesdatadir}/%{pname}/menu/*
%{_gamesdatadir}/%{pname}/tracks/road/aalborg/*
%{_gamesdatadir}/%{pname}/tracks/road/alpine-1/*
%{_gamesdatadir}/%{pname}/tracks/road/alpine-2/*
%{_gamesdatadir}/%{pname}/tracks/road/eroad/*
%{_gamesdatadir}/%{pname}/tracks/road/e-track-1/*
%{_gamesdatadir}/%{pname}/tracks/road/e-track-2/*
%{_gamesdatadir}/%{pname}/tracks/road/e-track-3/*
%{_gamesdatadir}/%{pname}/tracks/road/e-track-4/*
#%{_gamesdatadir}/%{pname}/tracks/road/e-track-5/*
%{_gamesdatadir}/%{pname}/tracks/road/e-track-6/*
%{_gamesdatadir}/%{pname}/tracks/road/forza/*
%{_gamesdatadir}/%{pname}/tracks/road/g-track-1/*
%{_gamesdatadir}/%{pname}/tracks/road/g-track-2/*
%{_gamesdatadir}/%{pname}/tracks/road/g-track-3/*
%{_gamesdatadir}/%{pname}/tracks/road/ole-road-1/*
%{_gamesdatadir}/%{pname}/tracks/road/ruudskogen/*
%{_gamesdatadir}/%{pname}/tracks/road/spring/*
%{_gamesdatadir}/%{pname}/tracks/road/street-1/*
%{_gamesdatadir}/%{pname}/tracks/road/wheel-1/*
%{_gamesdatadir}/%{pname}/tracks/road/wheel-2/*
%{_gamesdatadir}/%{pname}/tracks/oval/*
%{_gamesdatadir}/%{pname}/tracks/dirt/*
%{_gamesdatadir}/%{pname}/cars/car1-trb1/*
%{_gamesdatadir}/%{pname}/cars/car1-trb3/*
%{_gamesdatadir}/%{pname}/cars/car2-trb1/*
%{_gamesdatadir}/%{pname}/cars/car3-trb1/*
%{_gamesdatadir}/%{pname}/cars/car4-trb1/*
%{_gamesdatadir}/%{pname}/cars/car5-trb1/*
%{_gamesdatadir}/%{pname}/cars/car6-trb1/*
%{_gamesdatadir}/%{pname}/cars/car7-trb1/*
%{_gamesdatadir}/%{pname}/cars/p406/*
# %{_gamesdatadir}/%{pname}/cars/sc-f1/*
%{_gamesdatadir}/%{pname}/cars/car1-ow1/*
%{_gamesdatadir}/%{pname}/cars/car1-stock1/*
%{_gamesdatadir}/%{pname}/cars/car8-trb1/*
%{_gamesdatadir}/%{pname}/tracks/road/brondehach/*
%{_gamesdatadir}/%{pname}/tracks/road/corkscrew/*
%{_gamesdatadir}/%{pname}/wheels/*


%files cars-extra
%defattr(-, root, root)
%{_gamesdatadir}/torcs/cars/155-DTM/*
#%{_gamesdatadir}/torcs/cars/360-modena/*
%{_gamesdatadir}/torcs/cars/acura-nsx-sz/*
%{_gamesdatadir}/torcs/cars/baja-bug/*
%{_gamesdatadir}/torcs/cars/buggy/*
#%{_gamesdatadir}/torcs/cars/car1-trb1/*
#%{_gamesdatadir}/torcs/cars/clkdtm/*
#%{_gamesdatadir}/torcs/cars/gt40/*
#%{_gamesdatadir}/torcs/cars/lotus-gt1/*
#%{_gamesdatadir}/torcs/cars/mclaren-f1/*
#%{_gamesdatadir}/torcs/cars/p406/*
#%{_gamesdatadir}/torcs/cars/porsche-gt1/*
#%{_gamesdatadir}/torcs/cars/porsche-gt3rs/*
#%{_gamesdatadir}/torcs/cars/sc-f1/*
#%{_gamesdatadir}/torcs/cars/viper-gts-r/*
#%{_gamesdatadir}/torcs/cars/xj-220/*
%{_gamesdatadir}/torcs/cars/cg-nascar-rwd
%{_gamesdatadir}/torcs/categories/Nascar.xml
%{_gamesdatadir}/torcs/cars/pw-206wrc/*
%{_gamesdatadir}/torcs/cars/pw-306wrc/*
%{_gamesdatadir}/torcs/cars/pw-corollawrc/*
%{_gamesdatadir}/torcs/cars/pw-evoviwrc/*
#%{_gamesdatadir}/torcs/cars/pw-evovwrc/*
%{_gamesdatadir}/torcs/cars/pw-focuswrc/*
%{_gamesdatadir}/torcs/cars/pw-imprezawrc/*
%{_gamesdatadir}/torcs/cars/kc-2000gt/*
%{_gamesdatadir}/torcs/cars/kc-5300gt/*
%{_gamesdatadir}/torcs/cars/kc-corvette-ttop/*
%{_gamesdatadir}/torcs/cars/kc-daytona/*
%{_gamesdatadir}/torcs/cars/kc-db4z/*
%{_gamesdatadir}/torcs/cars/kc-dbs/*
%{_gamesdatadir}/torcs/cars/kc-dino/*
%{_gamesdatadir}/torcs/cars/kc-ghibli/*
%{_gamesdatadir}/torcs/cars/kc-grifo/*
%{_gamesdatadir}/torcs/cars/kc-bigh/*
%{_gamesdatadir}/torcs/cars/kc-a110/*
%{_gamesdatadir}/torcs/cars/kc-alfatz2/*
%{_gamesdatadir}/torcs/cars/kc-coda/*
%{_gamesdatadir}/torcs/cars/kc-conrero/*
%{_gamesdatadir}/torcs/cars/kc-gt40/*
%{_gamesdatadir}/torcs/cars/kc-gto/*
%{_gamesdatadir}/torcs/cars/kc-p4/*
%{_gamesdatadir}/torcs/cars/vm-x2/*
%{_gamesdatadir}/torcs/cars/vm-x4/*


%changelog
* Sun Feb 19 2012 Zombie Ryushu <ryushu@mandriva.org> 1.3.3-1
+ Revision: 777421
- install extra roads
- Remove missing car sc-f1
- Upgrade to 1.3.3

* Fri Feb 03 2012 Zombie Ryushu <ryushu@mandriva.org> 1.3.2-1
+ Revision: 771002
- Fix install stage
- Upgrade to 1.3.2
- Upgrade to 1.3.2

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 445518
- rebuild

* Tue Feb 10 2009 Zombie Ryushu <ryushu@mandriva.org> 1.3.1-1mdv2009.1
+ Revision: 339175
- Upgrade to 1.3.1

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.3.0-1mdv2008.1
+ Revision: 136550
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Nov 12 2006 Emmanuel Andry <eandry@mandriva.org> 1.3.0-1mdv2007.0
+ Revision: 83449
- New version 1.3.0

  + Lenny Cartier <lenny@mandriva.com>
    - Import torcs-data

