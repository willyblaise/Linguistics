use strict;
use warnings;
use Email::Address;

my $str = 'a@a.com;\"Tester, Test\" <test@example.com>,c@c.com;d@d.com';
my @addresses = Email::Address->parse($str);

foreach my $address (@addresses) {
    print $address->format . "\n";
}
