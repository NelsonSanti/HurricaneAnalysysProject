# Hurricane Analysis

In this project I have built a **set of functions** that organize and manipulate data about Category 5 Hurricanes (the strongest hurricanes as rated by their wind speed) in the American Atlantic Region:

- The first function, `updating_damages()` returns a list of updated damages where the recorded data from `damages` list is converted to float values while the missing data is retained as `"Damages not recorded"`.
- The second function `hurricanes_dictionary_by_name()` organizes the data collected on the _34 strongest Atlantic Hurricanes_.
- The third function `hurricanes_dictionary_by_year()` organizes each year with the correspondent attributes of the hurricanes in that year.
- The fourth function `counting_areas_affected()` counts the number of hurricanes by each area affected.
- The fifth function `most_affected_area()` finds the area affected by the most hurricanes, and how often it was it.
- The sixth function `greatest_number_of_deaths()` finds the hurricane that caused the greatest number of deaths, and how many deaths ir caused.
- The seventh function `hurricanes_mortality_scale()` rates hurricanes on a mortality scale according to **ratings from 1 to 5**, being _1_ the lowest rate, and _5_ the highest rate.
- The eighth function `greatest_damage()` finds the hurricane that caused the greatest damage, and how costly it was.
- The ninth and last function `how_much_damage()` rates hurricanes according to how much damage they caused.

> [!NOTE]
> There are many possible ways to correctly perform this project. This one was done according to my current knowledge.

Based on my functions' features I took the analysis beyond and used the `years` and the `damages` lists to create a plot that shows the _distribution_ and calculates the **mean** and the **median** of damage costs per year, which led me to the following output:

![Damage costs of the hurricanes by year](Hurricanes_project/damage_costs_of_the_hurricanes_by_year2.png)

In the `years` list there are some outliers like 125B, 91.6B, or 64.8B that are significantly affecting the mean, driving it to a value of 10.67B dollars annual damage cost, and making it much higher than the median. This is because the mean is sensitive to extreme values, while the median provides a better central tendency measure in such cases. The median value is 1.42B damage cost by year.

For cases like this it is recommended to use visualization through Box Plot rather than Scatter Plot, however, my focus was not on the outlier values. I visualy appreciate Scatter plots the most so i could rapidly explain what happend with the mean value and the high costs that are skewing the mean upwards.
