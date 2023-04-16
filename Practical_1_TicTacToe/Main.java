import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

class Node {

int value;
Node children[][]=new Node[3][3];
boolean isMin;
int field[][]=new int[3][3];

public Node(int field[][],boolean isMin) {
this.field=field;
this.isMin=isMin;
}

int[][] copyField() {
int[][] copied = new int[3][3];
for (int i = 0; i < copied.length; i++) {
for (int j = 0; j < copied[i].length; j++) {
copied[i][j] = field[i][j];
}
}
return copied;
}

public int learn() {

if(Main.hasWon(field)) {
value=isMin?1:-1;
return value;
}else if(Main.fieldFull(field)) {
value=0;
return value;
}
value=isMin?1:-1;

for(int i=0;i<field.length;i++) {
for(int j=0;j<field[0].length;j++) {
if(field[i][j]==0) {
int childField[][]=copyField();
childField[i][j]=isMin?1:2;
children[i][j]=new Node(childField,!isMin);
value=isMin? Math.min(value, children[i][j].learn()):Math.max(value, children[i][j].learn());

}
}
}
return value;
}

public Node getChildValue() {
for(int i=0;i<field.length;i++) {
for(int j=0;j<field[0].length;j++) {
if(children[i][j]!=null && children[i][j].value==value) {
return children[i][j];
}

}
}
return null;
}




}




public class Main{

static Scanner sc=new Scanner(System.in);
static int[][] field = new int[3][3];
static Node ai;
static int[][] magic = { { 8, 3, 4 }, { 1, 5, 9 }, { 6, 7, 2 } }; // magic board
static boolean player;
static ArrayList<Integer> playerMoves = new ArrayList<Integer>();
static ArrayList<Integer> movesToCounter = new ArrayList<Integer>();



static void printField(int[][] field) {
System.out.println(" _______");

for (int i = 0; i < field.length; i++) {
for (int j = 0; j < field[i].length; j++) {
System.out.print("|" + (field[i][j] == 0 ? "_" : field[i][j] == 1 ? "X" : "O") + "|");
}
System.out.println();
}
}

public static boolean hasWon(int[][] field) {
for (int i = 0; i < field.length; i++) {
if (field[i][0] == field[i][1] && field[i][1] == field[i][2] && field[i][0] != 0) {
return true;
}
if (field[0][i] == field[1][i] && field[1][i] == field[2][i] && field[0][i] != 0) {
return true;
}
}

if (field[0][0] == field[1][1] && field[1][1] == field[2][2] && field[0][0] != 0) {
return true;
}

if (field[0][2] == field[1][1] && field[1][1] == field[2][0] && field[0][2] != 0) {
return true;
}

return false;
}

private static int[] getInput() {
int value;
while(true) {
try {
value = Integer.parseInt(sc.next());
} catch (final Exception e) {
System.err.println("Enter an integer value");
continue;
}
value--;
if (value < 0 || value > 8) {
System.err.println("There is no such box");
continue;
}

final int row = value / 3;
final int col = value % 3;

if (field[row][col] != 0) {
System.err.println("Field is already set!");
continue;
}

return new int[] { row, col };

}

}

public static void clearField() {
for (int i = 0; i < field.length; i++) {
for (int j = 0; j < field.length; j++) {
field[i][j] = 0;
}

}
}

public static boolean fieldFull(int[][] field) {
for (int i = 0; i < field.length; i++) {
for (int j = 0; j < field.length; j++) {
if (field[i][j] == 0) {
return false;
}
}
}
return true;
}


public static int heuristicCounter(int field[][]) {
int D = 0;
int symbol=player==false?1:2;
for (int i = 0; i < field.length; i++) {
for (int j = 0; j < field[0].length; j++) {
if (field[i][j] == symbol && playerMoves.contains(magic[i][j]) == false) {
playerMoves.add(magic[i][j]);
}
}
}
for (int i = 0; i < playerMoves.size(); i++) {
for (int j = 0; j < playerMoves.size(); j++) {
if (i != j) {
D = 15 - playerMoves.get(i) - playerMoves.get(j);
if ((D >= 0 && D <= 9) && movesToCounter.contains(D) == false) {
movesToCounter.add(D);
return D;
}
}
}

}
return -1;
}


public static void main(String[] args) {

System.out.println("Enter Your Choice :\n 1: Player 1\n 2: Player 2");
int choice=sc.nextInt();
boolean isMin=choice==1? true:false;
ai=new Node(field,isMin);
ai.learn();
while(true){

Node current=ai;
player=isMin;
System.out.println("TicTacToe - Use 1-9 to set a field!");
printField(field);
while(true) {
System.out.println("Player " + (player ? "X" : "O") + " is about to set");
if(player) {
int indices[]=getInput();
field[indices[0]][indices[1]]=player?1:2;
current=current.children[indices[0]][indices[1]];
}else {
int result=heuristicCounter(field);
int row=-1,col=-1;
if(result!=-1 && playerMoves.size()>1){
for (int i = 0; i < magic.length; i++) {
for (int j = 0; j < magic[0].length; j++) {
if (magic[i][j] == result && field[i][j] == 0) {
row = i;
col = j;
}
}
}
if (row != -1 && col != -1) {
current = current.children[row][col];
}
else {
current=current.getChildValue();
}
}
else{
current=current.getChildValue();
}
}
field=current.copyField();
printField(field);
if (hasWon(field)) {
System.out.println("Player " + (player ? "X" : "O") + " won!\n");
break;
}

if (fieldFull(field)) {
System.out.println("It's a draw!\n");
break;
}
player = !player;

}
clearField();
}


}

}