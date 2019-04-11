import matplotlib.pyplot as plt

# TODO: plot what the camera sees (bw_img) and also line, filtered, and average peak

def show_frame(frame):
    # TODO have it show in the same frame, not a thousand of them
    plt.imshow(frame.array[:, :, 0])
    plt.show()

# plt.imshow(I)
# plt.plot(L, label="raw")
# plt.plot(Lf, label="filtered")
# plt.ylim([0, 300])
# plt.legend()
