Summary:	A software keyboard for SCIM
Name:		nagisa-keyboard
Version:	0.0.1
Release:	9
License:	GPLv2+
Group:		System/Internationalization
Url:		http://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bnagisa%5D%5D
Source0:	nagisa-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
Requires:	scim
BuildRequires:	qt3-devel
BuildRequires:	scim-devel

%description
Nagisa is a software keyboard for SCIM.

%files
%doc COPYING
%{_bindir}/*
%{_datadir}/nagisa/*

#----------------------------------------------------------------------------

%prep
%setup -q -n nagisa-%{version}

%build
%qmake_qt3 "PREFIX=/usr"
make

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/nagisa/

pushd src
	cp -f *.xml %{buildroot}%{_datadir}/nagisa/
	cp -f *.qm %{buildroot}%{_datadir}/nagisa/
	cp -f nagisa %{buildroot}%{_bindir}
popd

