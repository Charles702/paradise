import cv2
import math
import numpy as np

def FM_by_normalized_8_point(pts1, pts2):
    F, _ = cv2.findFundamentalMat(pts1, pts2, cv2.FM_8POINT)
    # comment out the above line of code.
    #number of points
    np = pts1.shape[1]
    #Normalize input points
    Pts1, T1 = NormalizeInput(pts1)
    Pts2, T2 = NormalizeInput(pts2)
    #construct the coefficient matrix
    C1 = Pts2[0]*Pts1[0]
    C2 = Pts2[0]*Pts1[1]
    C3 = Pts2[0]
    C4 = Pts2[1]*Pts1[0]
    C5 = Pts2[1]*Pts1[1]
    C6 = Pts2[1]
    C7 = Pts1[0]
    C8 = Pts1[1]
    C9 = np.ones([1, np])
    A = np.concatenate((C1,C2,C3,C4,C5,C6,C7,C8,C9), axis = 0)

    #Extract fundamental matrix from the column of V
    U, D, V = np.linalg.svd(A, full_matrices=True)
    print("V--"+V.shape)
    fMatrix = np.reshape(V[:][9],(3,3))

    #calculate fundamental matrix
    [U, S, V]= np.linalg.svd(fMatrix)
    F = np.matmul(np.matmul(U, np.diag([S[1][1], S[2][2], 0])),np.transpose(V))

    #Denormalise
    F = np.matmul(np.matmul(np.transpose(T2),fMatrix),T1)
    # F:  fundmental matrix
    return F

def NormalizeInput(pts):
    #get the Centroid
    centroid = pts.mean(1)
    # shift origin to centroid
    newpt = np.transpose(pts) - centroid

    meandis =  np.mean(np.sqrt(np.square(newpt[0])+ np.square(newpt[1])))
    scale = math.sqrt(2)/meandis

    TM = np.array([[scale, 0, (-1)*scale*centroid[0]],
                   [0, scale, (-1)*scale*centroid[1]],
                   [0, 0, 1]])
    normpts = np.matmul(TM,pts)
    return normpts

pts1 = np.array([4,8,32,45,70,21,4,7,8],[9,4,6,2,23,71,67,23,12])
pts2 = np.array([4,8,32,45,70,21,4,7,8],[9,4,6,2,23,71,67,23,12])

F, _ = cv2.findFundamentalMat(pts1, pts2, cv2.FM_8POINT)