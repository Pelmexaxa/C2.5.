# C2.5.

Задача для зачёта второго модуля на SkillBox C2.5. Итоговое практическое задание

Для работы с данным приложением нужно установить framework - Kivy
Гайд по установке Kivy:
https://kivy.org/doc/stable/gettingstarted/installation.html#installation-canonical


1 Во-первых, убедитесь, что инструменты python обновлены.
python -m pip install --upgrade pip wheel setuptools

2 Затем установите основные зависимости:
python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/

3 Стави Kivy:
python -m pip install kivy



P.S. Если вы используете Anaconda, вы можете установить Kivy с его менеджером пакетов Conda с помощью:
conda install kivy -c conda-forge
