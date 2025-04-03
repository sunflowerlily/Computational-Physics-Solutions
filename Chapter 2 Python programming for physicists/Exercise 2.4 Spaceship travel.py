import numpy as np

def how_much_time_to_reach(distance, speed_fraction_of_light):
    speed_of_light = 299792458
    distance = float(distance)
    speed_fraction_of_light = float(speed_fraction_of_light)

    # 计算飞船的实际速度
    ship_speed = speed_fraction_of_light * speed_of_light

    # 计算在驾驶舱内测量的时间
    time_in_cockpit = distance / ship_speed

    # 根据狭义相对论计算在地球上检测到的时间
    gamma = 1 / np.sqrt(1 - speed_fraction_of_light**2)
    time_on_earth = gamma * time_in_cockpit

    return time_in_cockpit, time_on_earth

if __name__ == "__main__":
    seconds_per_year = 365 * 24 * 3600  # 一年的秒数
    speed_of_light = 299792458  # 光速，单位：m/s
    distance = 10 * seconds_per_year * speed_of_light  # 10 光年的距离
    speed_fraction = 0.99  # 飞船速度是光速的 0.99 倍

    time_in_cockpit, time_on_earth = how_much_time_to_reach(distance, speed_fraction)
    # 将时间转换为年
    time_in_cockpit_in_years = time_in_cockpit / seconds_per_year
    time_on_earth_in_years = time_on_earth / seconds_per_year

    print(f"在飞船驾驶舱内测量的时间: {time_in_cockpit_in_years} 年，在地球上检测到的时间: {time_on_earth_in_years} 年")
    
