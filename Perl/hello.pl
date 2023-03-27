#!/bin/perl


use strict;
use warnings;
use feature qw(say);



print("Hello World\n");

my $name = "Champ";
my ($age, $street) = (40, '123 Main St');

my $my_info = "$name lives on \"$street\"\n";
$my_info = qq{$name lives on "$street"\n};

my %service = (

"Nicole" => 35,
"Champ" => 40
);

my $a = 5;
my $c = 10;

print("$a + $c = ", $a + $c , "\n");
my @names = ("champ", "pearl", "logan", "bray", "nicole");


foreach my $n (@names) {

	print "$n ";
}

print("\n");


print("Nicole is: ", $service{Nicole},"\n");

print $my_info;

system("java SalesTax");

sub get_random {
  return int(rand 11);
}

say "Random Number ", get_random();
