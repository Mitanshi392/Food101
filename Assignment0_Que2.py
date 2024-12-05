{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "20f46e20-0770-4335-9b33-3bc4ea384555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Choose the operation to be performed matrix\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "operator = input(\"Choose the operation to be performed\")\n",
    "ar1 = np.array([[1,2],[3,4]])\n",
    "ar2 = np.array([[1,2],[2,3]])        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "5e321946-d520-4442-90ce-be69db96e2bf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "the result is  [[ 5  8]\n",
      " [11 18]]\n"
     ]
    }
   ],
   "source": [
    "def matrix_operations(ar1,ar2,operator):\n",
    "    if operator == \"dot\":\n",
    "        if ar1.shape == ar2.shape :\n",
    "            result = ar1 * ar2\n",
    "            print(\"the result is \",result)\n",
    "        else:\n",
    "            print(\"dot product can't be performed\")\n",
    "    elif operator == \"matrix\":\n",
    "        if ar1.shape[1] == ar2.shape[0]:\n",
    "            array=[]\n",
    "            for r in range(0,ar1.shape[0]):\n",
    "                for c in range(0,ar2.shape[1]):\n",
    "                    array+=[sum(ar1[r] * ar2[:,c])]\n",
    "            a = np.array(array)\n",
    "            result = a.reshape([ar1.shape[0],ar2.shape[1]])\n",
    "            print(\"the result is \",result)\n",
    "        else:\n",
    "            print(\"Matrix multiplication cannot be performed\")\n",
    "            \n",
    "    elif operator == \"determinant\":\n",
    "        if ar1.shape[0] == ar1.shape[1] and ar2.shape[0] == ar2.shape[1]:\n",
    "            det1 = np.linalg.det(ar1)\n",
    "            det1 = np.linalg.det(ar2)\n",
    "            result = (det1,det2)\n",
    "            print(\"the result is \",result)\n",
    "        else:\n",
    "            print(\"contains a non-square matrix therefore determinant can not be computed\")\n",
    "\n",
    "matrix_operations(ar1,ar2,operator)\n",
    "\n",
    "\n",
    "        \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3acc241c-5dab-47b5-b4af-dba797e12dec",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
