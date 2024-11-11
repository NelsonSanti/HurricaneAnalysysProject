import matplotlib.pyplot as plt
import statistics

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 
         'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 
          'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 
         1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 
                       160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], 
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], 
                  ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], 
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
                  ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], 
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], 
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 
           'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', 
           '1.42B', '25.4M', 'Damages not recorded', '1.54B', 
           '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', 
           '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,
          2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
miliions_billions_conversion = list(conversion.values())
#print(miliions_billions_conversion)
def updating_damages():
  updated_damages = []
  for data in damages:
    if 'Damages not recorded' in data:
      updated_damages.append(data)
    if 'M' in data:
      data_without_m = data.strip('MB')
      float_data_m = float(data_without_m)
      multiplied_m = float_data_m*miliions_billions_conversion[0]
      updated_damages.append(multiplied_m)
    elif 'B' in data:
      data_without_b = data.strip('MB')
      float_data_b = float(data_without_b)
      multiplied_b = float_data_b*miliions_billions_conversion[1]
      updated_damages.append(multiplied_b)
  return updated_damages

new_data_about_damages = updating_damages()
#print(new_data_about_damages)

# 2 
# Create a Table
names_of_the_hurricanes = names
# Create and view the hurricanes dictionary
def hurricanes_dictionary_by_name():
  hurricanes = {}
  for i in range(len(names_of_the_hurricanes)):
    inside_dict = {"Name": names[i], 
    "Month": months[i], 
    "Year": years[i], 
    "Max Sustained Wind": max_sustained_winds[i], 
    "Areas Affected": areas_affected[i], 
    "Damage": new_data_about_damages[i], 
    "Deaths": deaths[i]}
    hurricanes[names_of_the_hurricanes[i]] = inside_dict
  return hurricanes
#print(hurricanes_dictionary_by_name())

# 3
# Organizing by Year
year_of_the_hurricane = years
# create a new dictionary of hurricanes with year and key
def hurricanes_dictionary_by_year():
  hurricane_by_year = {}
  for i in range(len(year_of_the_hurricane)):
    inside_dict = {"Name": names[i], 
    "Month": months[i], 
    "Year": years[i], 
    "Max Sustained Wind": max_sustained_winds[i], 
    "Areas Affected": areas_affected[i], 
    "Damage": new_data_about_damages[i], 
    "Deaths": deaths[i]}
    hurricane_by_year[year_of_the_hurricane[i]] = inside_dict
  return hurricane_by_year
print(hurricanes_dictionary_by_year())

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def counting_areas_affected():
  count_of_areas_affected = {}
  for i in range(len(areas_affected)):
    for j in areas_affected[i]:
      if j in count_of_areas_affected:
        count_of_areas_affected[j] +=1
      else:
        count_of_areas_affected[j] = 1
  return count_of_areas_affected
#print(counting_areas_affected())

# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area():
  max_area = 'Central America'
  max_area_count = 0
  for key, value in counting_areas_affected().items():
    if max_area_count < value:
      max_area = key
      max_area_count = value
  return max_area, max_area_count

result1, result2 = most_affected_area()
#print(result1, result2)

# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def greatest_number_of_deaths():
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for key, value in hurricanes_dictionary_by_name().items():
    if max_mortality < value['Deaths']:
      max_mortality_cane = key
      max_mortality = value['Deaths']
  return max_mortality_cane, max_mortality
result3, result4 = greatest_number_of_deaths()
#print(result3, result4)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000,
                   5: 100000}
# categorize hurricanes in new dictionary with mortality severity as key
def hurricanes_mortality_scale():
  hurricanes_by_mortality = {}
  for key, value in mortality_scale.items():
    hurricanes_by_mortality[key]=[]
  for value in hurricanes_dictionary_by_name().values():
    deaths = value['Deaths']
    if deaths > 0 and deaths <= 100:
      hurricanes_by_mortality[1].append(value['Deaths'])
    elif deaths > 100 and deaths <= 500:
      hurricanes_by_mortality[2].append(value['Deaths'])
    elif deaths > 500 and deaths <= 1000:
      hurricanes_by_mortality[3].append(value['Deaths'])
    elif deaths > 1000 and deaths <= 10000:
      hurricanes_by_mortality[4].append(value['Deaths'])
    elif deaths > 10000 and deaths <= 100000:
      hurricanes_by_mortality[5].append(value['Deaths'])
  return hurricanes_by_mortality
#print(hurricanes_mortality_scale())

# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def greatest_damage():
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for key, value in hurricanes_dictionary_by_name().items():
    damages = value['Damage']
    if damages == 'Damages not recorded':
      continue
    elif max_damage < damages:
      max_damage_cane = key
      max_damage = damages
  return max_damage_cane, max_damage
result5, result6 = greatest_damage()
#print(result5, result6)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key
def how_much_damage():
  cost_by_damage = {}
  for key, value in damage_scale.items():
    cost_by_damage[key]=[]
  for value in hurricanes_dictionary_by_name().values():
    damages = value['Damage']
    if isinstance(damages, (int, float)):
      if damages > 0 and damages <= 100000000:
        cost_by_damage[1].append(value['Damage'])
      elif damages > 100000000 and damages <= 1000000000:
        cost_by_damage[2].append(value['Damage'])
      elif damages > 1000000000 and damages <= 10000000000:
        cost_by_damage[3].append(value['Damage'])
      elif damages > 10000000000 and damages <= 50000000000:
        cost_by_damage[4].append(value['Damage'])
  return cost_by_damage
#print(how_much_damage())

#Hurricanes Analysis visualization
#Damage costs of Hurricanes for each year

#Getting the hurricanes data by costs from the correspondent function

hurricane_costs = updating_damages()

#Creating a new dictionary that counts the damage costs of the hurricanes by year (using the years list directly)

counting_costs = {}
for i in range(len(years)):
    year = years[i]
    cost = hurricane_costs[i]
    if cost != 'Damages not recorded':
        if cost in counting_costs:
            counting_costs[year] += cost
        else:
            counting_costs[year] = cost

#Creating the plot
year_axis = list(counting_costs.keys())
costs_axis = list(counting_costs.values())

# Calculate mean and median
mean_cost = statistics.mean(costs_axis)
median_cost = statistics.median(costs_axis)

plt.style.use('ggplot')
#ggplot style automatically includes grid lines, 
#but plt.grid(True) can be used to ensure grid lines are present with any style.
plt.figure(figsize=(10, 6))
plt.scatter(year_axis, costs_axis, c=costs_axis, cmap='viridis', s=100, alpha=0.7, edgecolors='w')
#c=costs_axis - assigns colors to the points based on their values
#cmap='color_map': c=costs colors are tailored according to cmap cost intensity
#s=number sets the marker size
#alpha=number adjusts marker transparency
#edgecolors='w' adds white edge colors to markers (for better contrast)
plt.axhline(y=mean_cost, color='r', linestyle='--', label=f'Mean: {mean_cost:.2f}')
plt.axhline(y=median_cost, color='b', linestyle='-', label=f'Median: {median_cost:.2f}')
plt.legend()
plt.title('Hurricanes Costs by Year')
plt.xlabel('Years')
plt.ylabel('Costs in USD')
plt.colorbar(label='Cost Intensity')
#plt.grid(True)
#grid(True) adds grid lines to the plot improving readability by aligning the points with the axes.
plt.show()
