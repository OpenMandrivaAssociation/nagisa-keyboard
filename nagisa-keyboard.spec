%define src_name  nagisa

%define scim_version   1.4.2

Name:      nagisa-keyboard
Summary:   A software keyboard for SCIM
Version:   0.0.1
Release:   9
Group:     System/Internationalization
License:   GPL
URL:       http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bnagisa%5D%5D
Source0:   %{src_name}-%{version}.tar.bz2
Source1:   %{name}.rpmlintrc
Requires:        scim >= %{scim_version}
BuildRequires:   qt3-devel
BuildRequires:   scim-devel

%description
Nagisa is a software keyboard for SCIM.


%prep
%setup -q -n %{src_name}-%{version}

%build
qmake "PREFIX=/usr"
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/nagisa/

cd src/
	cp -f *.xml $RPM_BUILD_ROOT/%{_datadir}/nagisa/
	cp -f *.qm $RPM_BUILD_ROOT/%{_datadir}/nagisa/
	cp -f nagisa $RPM_BUILD_ROOT/%{_bindir}
cd -

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING
%{_bindir}/*
%{_datadir}/nagisa/*


%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.1-8mdv2011.0
+ Revision: 620473
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.1-7mdv2010.0
+ Revision: 430150
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.0.1-6mdv2009.0
+ Revision: 241054
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Sep 06 2007 Thierry Vignaud <tv@mandriva.org> 0.0.1-4mdv2008.0
+ Revision: 80676
- drop require already catched by autoprov and which is wrong on x86_64 anyway

* Wed Sep 05 2007 Thierry Vignaud <tv@mandriva.org> 0.0.1-3mdv2008.0
+ Revision: 80322
- rebuild
- Import nagisa-keyboard




* Wed Dec 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.0.1-2mdk
- Fix BuildRequires

* Wed Nov 16 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.0.1-1mdk
- new release

* Sat Oct 29 2005 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.0.0-1mdk
- first spec for Mandriva Linux
