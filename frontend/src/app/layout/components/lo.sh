#!/bin/bash

# List of feature module names
modules="bodychart
cards
charts
dark
footer
landing
layout
list
loaders
notification
search-suggest
searchbar
sidenav
sign-in-up
stepper
swipe"

# Loop through each module name and run ng generate module command
for module in $modules; do
    ng generate module $module --route $module --module app.module
done
