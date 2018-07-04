%define 	fname	SimpleTAL
%define		module	%(echo %{fname} | tr A-Z a-z)

Summary:	Stand alone implementation of the TAL, TALES and METAL specifications
Summary(pl.UTF-8):	Niezależna implementacja specyfikacji TAL, TALES i METAL
Name:		python-simpletal
# Don't upgrade to anything newer since newer versions are for python3. Use python3-simpletal for that.
Version:	4.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://www.owlfish.com/software/simpleTAL/downloads/%{fname}-%{version}.tar.gz
# Source0-md5:	147035bae18e4d37aea26c7d2019a0d2
URL:		http://www.owlfish.com/software/simpleTAL/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and
METAL specifications used in Zope to power HTML and XML templates.
SimpleTAL is an independent implementation of TAL; there are no
dependencies on Zope nor is any of the Zope work re-used.

%description -l pl.UTF-8
SimpleTAL to samodzielna implementacja specyfikacji TAL, TALES i METAL
używanych w Zope do wspomagania szablonów HTML i XML. SimpleTAL to
niezależna implementacja TAL; nie zależy od Zope i nie jest ponownym
użyciem żadnej z prac Zope.

%package examples
Summary:	Example files for SimpleTAL
Summary(pl.UTF-8):	Pliki przykładów dla SimpleTAL
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for SimpleTAL. 

%description examples -l pl.UTF-8
Pliki przykładów dla SimpleTAL.

%prep
%setup -q -n %{fname}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/ -name \*.py | xargs rm -f

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt README.txt documentation/html
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-*.egg-info

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
