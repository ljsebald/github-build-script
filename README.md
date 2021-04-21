# GitHub Classroom Kernel Build Script
Build scripts for dealing with kernel builds on GitHub classroom as used
in UMBC's CMSC 421 class.

## Notes
Please note that this script requires an input JSON document of the
repositories to consider for building. Each JSON element must have the
following elements:

string name    - Name of the repository

string ssh_url - SSH URL of the remote declaration

No other elements are necessary, however if other elements are present,
they will be ignored.

You will need to obtain this information either manually or by using the
appropriate GitHub API calls to do so.

This script requires Python 2.7 and will require some work to up-port to
Python 3.x. The author highly recommends that anyone considering using
this work undertake the effort to up-port this to Python 3.x. If you do
so, feel free to submit a PR to update the script.

## Disclaimer
This code was not produced for hire at UMBC, but rather was produced on
the author's own time to make his job as a TA easier. The author makes no
claim that this script has any use outside of that task and also makes no
claim that the script still functions as designed or will continue to do
so in the future.

## License
Copyright (C) 2016-2021 Lawrence Sebald

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License version 3
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
