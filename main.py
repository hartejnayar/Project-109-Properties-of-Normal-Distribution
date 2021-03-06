import statistics
import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")

math_score_list = df["math score"].to_list()
reading_score_list = df["reading score"].to_list()
writing_score_list = df["writing score"].to_list()

math_score_mean = statistics.mean(math_score_list)
reading_score_mean = statistics.mean(reading_score_list)
writing_score_mean = statistics.mean(writing_score_list)

math_score_median = statistics.median(math_score_list)
reading_score_median = statistics.median(reading_score_list)
writing_score_median = statistics.median(writing_score_list)

math_score_mode = statistics.mode(math_score_list)
reading_score_mode = statistics.mode(reading_score_list)
writing_score_mode = statistics.mode(writing_score_list)


print("Mean, median and mode of math score --> {}, {}, {}\nMean, median and mode of reading score --> {}, {}, {}\nMean, median, mode of writing score --> {}, {}, {}".format(
    math_score_mean, math_score_median, math_score_mode,
    reading_score_mean, reading_score_median, reading_score_mode,
    writing_score_mean, writing_score_median, writing_score_mode))


math_score_standard_deviation = statistics.stdev(math_score_list)
reading_score_standard_deviation = statistics.stdev(reading_score_list)
writing_score_standard_deviation = statistics.stdev(writing_score_list)

math_score_1st_standard_deviation_start, math_score_1st_standard_deviation_end = math_score_mean - math_score_standard_deviation, math_score_mean + math_score_standard_deviation
reading_score_1st_standard_deviation_start, reading_score_1st_standard_deviation_end = reading_score_mean - reading_score_standard_deviation, reading_score_mean + reading_score_standard_deviation
writing_score_1st_standard_deviation_start, writing_score_1st_standard_deviation_end = writing_score_mean - writing_score_standard_deviation, writing_score_mean + writing_score_standard_deviation

math_score_2nd_standard_deviation_start, math_score_2nd_standard_deviation_end = math_score_mean - (2 * math_score_standard_deviation), math_score_mean + (2 * math_score_standard_deviation)
reading_score_2nd_standard_deviation_start, reading_score_2nd_standard_deviation_end = reading_score_mean - (2 * reading_score_standard_deviation), reading_score_mean + (2 * reading_score_standard_deviation)
writing_score_2nd_standard_deviation_start, writing_score_2nd_standard_deviation_end = writing_score_mean - (2 * writing_score_standard_deviation), writing_score_mean + (2 * writing_score_standard_deviation)

math_score_3rd_standard_deviation_start, math_score_3rd_standard_deviation_end = math_score_mean - (3 * math_score_standard_deviation), math_score_mean + (3 * math_score_standard_deviation)
reading_score_3rd_standard_deviation_start, reading_score_3rd_standard_deviation_end = reading_score_mean - (3 * reading_score_standard_deviation), reading_score_mean + (3 * reading_score_standard_deviation)
writing_score_3rd_standard_deviation_start, writing_score_3rd_standard_deviation_end = writing_score_mean - (3 * writing_score_standard_deviation), writing_score_mean + (3 * writing_score_standard_deviation)

math_score_list_1_standard_deviation = [result for result in math_score_list if result > math_score_1st_standard_deviation_start and result < math_score_1st_standard_deviation_end]
math_score_list_2_standard_deviation = [result for result in math_score_list if result > math_score_2nd_standard_deviation_start and result < math_score_2nd_standard_deviation_end]
math_score_list_3_standard_deviation = [result for result in math_score_list if result > math_score_3rd_standard_deviation_start and result < math_score_3rd_standard_deviation_end]

reading_score_list_1_standard_deviation = [result for result in reading_score_list if result > reading_score_1st_standard_deviation_start and result < reading_score_1st_standard_deviation_end]
reading_score_list_2_standard_deviation = [result for result in reading_score_list if result > reading_score_2nd_standard_deviation_start and result < reading_score_2nd_standard_deviation_end]
reading_score_list_3_standard_deviation = [result for result in reading_score_list if result > reading_score_3rd_standard_deviation_start and result < reading_score_3rd_standard_deviation_end]

writing_score_list_1_standard_deviation = [result for result in writing_score_list if result > writing_score_1st_standard_deviation_start and result < writing_score_1st_standard_deviation_end]
writing_score_list_2_standard_deviation = [result for result in writing_score_list if result > writing_score_2nd_standard_deviation_start and result < writing_score_2nd_standard_deviation_end]
writing_score_list_3_standard_deviation = [result for result in writing_score_list if result > writing_score_3rd_standard_deviation_start and result < writing_score_3rd_standard_deviation_end]

math_score_fig = ff.create_distplot([math_score_list],["math score"], show_hist=False)
math_score_fig.add_trace(go.Scatter(x=[math_score_mean,math_score_mean],y=[0,0.2],mode="lines",name="MEAN"))
math_score_fig.add_trace(go.Scatter(x=[math_score_1st_standard_deviation_start, math_score_1st_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
math_score_fig.add_trace(go.Scatter(x=[math_score_1st_standard_deviation_end, math_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
math_score_fig.add_trace(go.Scatter(x=[math_score_2nd_standard_deviation_start, math_score_2nd_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
math_score_fig.add_trace(go.Scatter(x=[math_score_1st_standard_deviation_end, math_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
math_score_fig.show()

reading_score_fig = ff.create_distplot([reading_score_list],["reading score"], show_hist=False)
reading_score_fig.add_trace(go.Scatter(x=[reading_score_mean,reading_score_mean],y=[0,0.2],mode="lines",name="MEAN"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_1st_standard_deviation_start, reading_score_1st_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_1st_standard_deviation_end, reading_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_2nd_standard_deviation_start, reading_score_2nd_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
reading_score_fig.add_trace(go.Scatter(x=[reading_score_1st_standard_deviation_end, reading_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
reading_score_fig.show()

writing_score_fig = ff.create_distplot([writing_score_list],["writing score"], show_hist=False)
writing_score_fig.add_trace(go.Scatter(x=[writing_score_mean,writing_score_mean],y=[0,0.2],mode="lines",name="MEAN"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_1st_standard_deviation_start, writing_score_1st_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_1st_standard_deviation_end, writing_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_2nd_standard_deviation_start, writing_score_2nd_standard_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
writing_score_fig.add_trace(go.Scatter(x=[writing_score_1st_standard_deviation_end, writing_score_1st_standard_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
writing_score_fig.show()

print("\n{}% of data for math score lies within 1 standard deviation ".format(len(math_score_list_1_standard_deviation) * 100.0 / len(math_score_list)))
print("{}% of data for math score lies within 2 standard deviations ".format(len(math_score_list_2_standard_deviation) * 100.0 / len(math_score_list)))
print("{}% of data for math score lies within 3 standard deviations ".format(len(math_score_list_3_standard_deviation) * 100.0 / len(math_score_list)))

print("\n{}% of data for reading score lies within 1 standard deviation ".format(len(reading_score_list_1_standard_deviation) * 100.0 / len(reading_score_list)))
print("{}% of data for reading score lies within 2 standard deviations ".format(len(reading_score_list_2_standard_deviation) * 100.0 / len(reading_score_list)))
print("{}% of data for reading score lies within 3 standard deviations ".format(len(reading_score_list_3_standard_deviation) * 100.0 / len(reading_score_list)))

print("\n{}% of data for writing score lies within 1 standard deviation ".format(len(writing_score_list_1_standard_deviation) * 100.0 / len(writing_score_list)))
print("{}% of data for writing score lies within 2 standard deviations ".format(len(writing_score_list_2_standard_deviation) * 100.0 / len(writing_score_list)))
print("{}% of data for writing score lies within 3 standard deviations ".format(len(writing_score_list_3_standard_deviation) * 100.0 / len(writing_score_list)))