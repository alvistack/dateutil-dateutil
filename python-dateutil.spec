# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-dateutil
Epoch: 100
Version: 2.8.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Powerful extensions to the standard datetime module
License: Apache-2.0
URL: https://github.com/dateutil/dateutil/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
The dateutil module provides powerful extensions to the standard
datetime module available in Python.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-python-dateutil
Summary: Powerful extensions to the standard datetime module
Requires: python3
Requires: python3-six >= 1.5
Requires: timezone
Provides: python3-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-python-dateutil
The dateutil module provides powerful extensions to the standard
datetime module available in Python.

%files -n python%{python3_version_nodots}-python-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-python-dateutil
Summary: Powerful extensions to the standard datetime module
Requires: python3
Requires: python3-six >= 1.5
Requires: timezone
Provides: python3-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python3-python-dateutil
The dateutil module provides powerful extensions to the standard
datetime module available in Python.

%files -n python3-python-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-dateutil
Summary: Powerful extensions to the standard datetime module
Requires: python3
Requires: python3-six >= 1.5
Requires: tzdata
Provides: python3-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dateutil) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-dateutil
The dateutil module provides powerful extensions to the standard
datetime module available in Python.

%files -n python%{python3_version_nodots}-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000) && !(0%{?rhel} == 7)
%package -n python3-dateutil
Summary: Powerful extensions to the standard datetime module
Requires: python3
Requires: python3-six >= 1.5
Requires: tzdata
Provides: python3-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python3dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(python-dateutil) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-python-dateutil = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(python-dateutil) = %{epoch}:%{version}-%{release}

%description -n python3-dateutil
The dateutil module provides powerful extensions to the standard
datetime module available in Python.

%files -n python3-dateutil
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
