#!/bin/bash

ENV_FOR_PYTHON2="virtualenv_for_python2.7"
ENV_FOR_PYTHON3="virtualenv_for_python3.7"
VERSION_PYTHON2="2.7.16"
VERSION_PYTHON3="3.7.3"

# check and install required packages
declare -a REQUIRED_PACKAGES=(git
                              patch
                              zlib-devel
                              bzip2 bzip2-devel
                              readline-devel
                              sqlite sqlite-devel
                              openssl-devel
                              xz xz-devel
                              libffi-devel
                              findutils
                             )

for package in ${REQUIRED_PACKAGES[@]}; do
    if [[ $(rpm -qa | grep -cP "${package}-\d+") -eq 0 ]]; then
        echo "$package is not installed."
        sudo yum install -y $package
    fi
done

# check and install pyenv
if [[ $(whereis pyenv | grep -cP "pyenv: .+") -eq 0 ]]; then
    curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

    export PATH=""$(eval echo ~$USER)"/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    # for autostart
    echo "export PATH=\""$(eval echo ~$USER)"/.pyenv/bin:\$PATH\"" >> "$(eval echo ~$USER)"/.bashrc
    echo "eval \"\$(pyenv init -)\"" >> "$(eval echo ~$USER)"/.bashrc
    echo "eval \"\$(pyenv virtualenv-init -)\"" >> "$(eval echo ~$USER)"/.bashrc

fi

# install Python 2.7 and Python 3.7
if [[ $(pyenv versions | grep -c "$VERSION_PYTHON2") -eq 0 ]]; then
    pyenv install "$VERSION_PYTHON2"
fi

if [[ $(pyenv versions | grep -c "$VERSION_PYTHON3") -eq 0 ]]; then
    pyenv install "$VERSION_PYTHON3"
fi

# create virtualenv environments
if [[ $(pyenv versions | grep -c "/envs/"$ENV_FOR_PYTHON2"") -eq 0 ]]; then
    pyenv virtualenv "$VERSION_PYTHON2" "$ENV_FOR_PYTHON2"
else
    echo "Sorry. You have "$ENV_FOR_PYTHON2"."
fi

if [[ $(pyenv versions | grep -c "/envs/"$ENV_FOR_PYTHON2"") -eq 0 ]]; then
    pyenv virtualenv "$VERSION_PYTHON3" "$ENV_FOR_PYTHON3"
else
    echo "Sorry. You have "$ENV_FOR_PYTHON3"."
fi
