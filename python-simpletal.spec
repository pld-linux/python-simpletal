%define 	fname	SimpleTAL
%define		module	%(echo %{fname} | tr A-Z a-z)

Summary:	Stand alone implementation of the TAL, TALES and METAL specifications
Summary(pl):	Niezale�na implementacja specyfikacji TAL, TALES i METAL
Name:		python-%{module}
Version:	3.12
Release:	0.1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://www.owlfish.com/software/simpleTAL/downloads/%{fname}-%{version}.tar.gz
# Source0-md5:	4c34dc80dba22d9f7ea7ff7fd2e2bea1
URL:		http://www.owlfish.com/software/simpleTAL/
BuildRequires:	python
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SimpleTAL is a stand alone Python implementation of the TAL, TALES and
METAL specifications used in Zope to power HTML and XML templates.
SimpleTAL is an independent implementation of TAL; there are no
dependencies on Zope nor is any of the Zope work re-used.

%description -l pl
SimpleTAL to samodzielna implementacja specyfikacji TAL, TALES i METAL
u�ywanych w Zope do wspomagania szablon�w HTML i XML. SimpleTAL to
niezale�na implementacja TAL; nie zale�y od Zope i nie jest ponownym
u�yciem �adnej z prac Zope.

%package examples
Summary:	Example files for SimpleTAL
Summary(pl):	Pliki przyk�ad�w dla SimpleTAL
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description examples
Example files for SimpleTAL. 

%description examples -l pl
Pliki przyk�ad�w dla SimpleTAL.

%prep
%setup -q -n %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/%{module}/ -name \*.py | xargs rm -f

cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt README.txt documentation/html
%{py_sitescriptdir}/%{module}

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
