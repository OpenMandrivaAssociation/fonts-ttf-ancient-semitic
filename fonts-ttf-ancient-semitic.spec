%define upstream_name		AncientSemiticFonts
%define	upstream_version	0.06-1

%define rname		ancient-semitic
%define ver		0.06.1
%define rel		2

%define _fontdir	%{_datadir}/fonts/TTF

%define debug_package	%{nil}

Name:		fonts-ttf-%{rname}
Version:	%{ver}
Release:	%mkrel %{rel}
Summary:	A collection of fonts related to the history of the Hebrew writing
Url:		http://culmus.sourceforge.net/ancient/index.html
License:	GPLv2
Source0:	http://sourceforge.net/downloads/project/culmus/ancient_fonts/%{upstream_name}-%{upstream-version}/%{upstream_name}-%{upstream_version}.tgz
Source1:	GenerateTTF.pe
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	fontforge
BuildRequires:	ttmkfdir
Provides:	ancient-semitic-fonts = %{version}-%{release}

%description
This package contains a collection of fonts related to the
history of the Hebrew writing. Starting with the Proto-Canaanite
continuing with Phoenician/Canaanite, Paleo-Hebrew, Aramaic, early
Hebrew Square Script - all the way to the modern Hebrew letter forms. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

#fix rights 
chmod 644 README LICENSE CHANGES

#build fonts from source
rm -rf src/*.ttf

%build
pushd src
install -m755 %{SOURCE1} .
for i in *.sfd
	do ./GenerateTTF.pe $i .
done
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_fontdir}/AncientSemitic
cp src/*.ttf %{buildroot}%{_fontdir}/AncientSemitic

ttmkfdir -d %{buildroot}%{_fontdir}/AncientSemitic -o %{buildroot}%{_fontdir}/AncientSemitic/fonts.dir
ln -s fonts.dir %{buildroot}%{_fontdir}/AncientSemitic/fonts.scale

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE CHANGES
%{_fontdir}/AncientSemitic


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 0.06.1-2mdv2011.0
+ Revision: 675514
- br fontconfig for fc-query used in new rpm-setup-build

* Tue Nov 09 2010 Jani Välimaa <wally@mandriva.org> 0.06.1-1mdv2011.0
+ Revision: 595453
- import fonts-ttf-ancient-semitic

