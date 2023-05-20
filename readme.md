# godot .tscn linter

This is a very simple Python tool for quickly getting through annoying, cryptic errors with corrupted Godot .tscn files.
Pass the .tscn file to main.py, and it should just work.

It checks for proper initialization of ext and subresources, and the existence of all the ext_resource paths in the file.
