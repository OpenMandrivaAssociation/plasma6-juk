Summary:	A music player and manager for KDE
Name:		plasma6-juk
Version:	24.01.85
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/multimedia/juk/
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/juk-%{version}.tar.xz
BuildRequires:	pkgconfig(taglib) >= 1.7
BuildRequires:	ninja
BuildRequires:	appstream
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GlobalAccel)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6JobWidgets)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6WindowSystem)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(Phonon4Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)

# Tunepimp support hasn't been ported to KDE6
BuildConflicts:	libtunepimp-devel

%description
JuK is an audio jukebox application, supporting collections of MP3, Ogg
Vorbis, and FLAC audio files. It allows you to edit the "tags" of your
audio files, and manage your collection and playlists. It's main focus,
in fact, is on music management.

%files -f juk.lang
%{_bindir}/juk
%{_datadir}/kxmlgui6/juk
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/metainfo/*.xml
%{_datadir}/applications/org.kde.juk.desktop
%{_datadir}/dbus-1/interfaces/org.kde.juk.*.xml
%{_datadir}/juk
%{_datadir}/knotifications6/juk.notifyrc
%{_datadir}/kio/servicemenus/jukservicemenu.desktop

#------------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
ninja -C build

%install
%ninja_install -C build
%find_lang juk --all-name --with-html