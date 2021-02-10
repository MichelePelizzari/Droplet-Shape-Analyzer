# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:05:57 2021

@author: s2033647
"""
import imageio
import matplotlib.pyplot as plt
import cv2
import numpy as np
import scipy.interpolate as spint

# Import the image

image = imageio.imread('SOCAL_1.png')

# Display the image as it is

plt.figure()
plt.imshow(image)
plt.colorbar()
plt.show()

# Display a focus on the droplet

image = image[500:900, 300:1000]
plt.figure()
plt.imshow(image)
plt.show()
              
# Recognize the edges and plot them

thres1 = image.min()
thres2 = image.max()
edges = cv2.Canny(image, thres1, thres2)

plt.figure()
plt.imshow(edges)
plt.show()

# Increase the thresholds for the brightness

thres1 = image.min()*0.75
thres2 = image.max()*1.5
edges = cv2.Canny(image, thres1, thres2)

plt.figure()
plt.imshow(edges)
plt.show()

#edges[180:, :] = 0

# Display the edges
plt.figure()
plt.imshow(edges)
plt.show()

# DIsplay the points for the edges

ys, xs = np.where(edges)
ys = np.asarray(-ys, dtype=float)
xs = np.asarray(xs, dtype=float)

plt.figure()
plt.plot(xs, ys, marker=',', ls='none')
plt.axis('equal')
plt.show()

# Center the image

xs = xs - xs.mean()
ys = ys - ys.min()

plt.figure()
plt.plot(xs, ys, marker=',', ls='none')
plt.axis('equal')
plt.show()

# Fit the points with a polyline --- not useful at the moment


# new_xs = np.sort(list(set(xs)))
# new_ys = []
# for x in new_xs:
#     new_ys.append(np.mean(ys[xs == x]))
# xs = new_xs
# ys = np.asarray(new_ys)

# # Fitting the drop edge

# edge_f = spint.UnivariateSpline(xs, ys, k=5, s=0.005)

# # Display the fit
# fig, axs = plt.subplots(1, 2, figsize=(10, 4))
# plt.sca(axs[0])
# plt.plot(xs, ys, marker='o', ls='none')
# plt.plot(xs, edge_f(xs))
# plt.axhline(0, color='k')
# plt.xlabel('x [mm]')
# plt.ylabel('y [mm]')
# plt.axis('equal')
# # Plot a zoom on the edge
# plt.sca(axs[1])
# plt.plot(xs, ys, marker='o', ls='none')
# plt.plot(xs, edge_f(xs))
# plt.axhline(0, color='k')
# plt.axis('equal')
# plt.xlabel('x [mm]')
# plt.xlim(-1.1, -0.7)
# plt.ylim(0, 0.5)
# plt.title("Zoom")
# plt.show()