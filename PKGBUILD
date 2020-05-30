# Maintainer: Gregory Clark <gianator@gianator.me>
pkgname=sshaman-git
_pkgname=sshaman
pkgver=0.r38.cfb8bb4
pkgrel=1
pkgdesc="A simple ssh manager"
arch=('any')
url="https://github.com/gianator/sshaman.git"
license=('GPL3')
depends=(python)
makedepends=(git make python-setuptools)
optdepends=()
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("git+$url")
md5sums=('SKIP')

pkgver() {
	cd "$_pkgname"
	printf "0.r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	cd "$_pkgname"
	python setup.py install --root="$pkgdir"
}
