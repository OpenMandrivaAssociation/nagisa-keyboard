%define version   0.0.1
%define release   %mkrel 7
%define src_name  nagisa

%define scim_version   1.4.2

Name:      nagisa-keyboard
Summary:   A software keyboard for SCIM
Version:   %{version}
Release:   %{release}
Group:     System/Internationalization
License:   GPL
URL:       http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bnagisa%5D%5D
Source0:   %{src_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
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
rm -rf $RPM_BUILD_ROOT

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
%defattr(-,root,root)
%doc COPYING
%{_bindir}/*
%{_datadir}/nagisa/*
